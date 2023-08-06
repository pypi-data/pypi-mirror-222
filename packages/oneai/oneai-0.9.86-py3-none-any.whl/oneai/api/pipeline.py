from datetime import timedelta
import io
import json
import urllib.parse
from typing import Awaitable, List

import aiohttp
import oneai, oneai.api
from oneai.api.output import build_output
from oneai.classes import Input, Skill, CSVParams
from oneai.output import Output
from oneai.exceptions import handle_unsuccessful_response, validate_api_key

endpoint_default = "api/v0/pipeline"
endpoint_async = "api/v0/pipeline/async"
endpoint_async_file = "api/v0/pipeline/async/file"
endpoint_async_tasks = "api/v0/pipeline/async/tasks"


def build_request(
    input: Input,
    steps: List[Skill],
    multilingual: bool,
    include_text: bool,
    csv_params: CSVParams = None,
):
    def json_default(obj):
        if isinstance(obj, timedelta):
            return str(obj)
        if isinstance(obj, Skill):
            return obj.api_name
        return {k: v for k, v in obj.__dict__.items() if v is not None}

    # use input metadata for clustering
    if hasattr(input, "metadata"):
        for skill in steps:
            if skill.api_name == "clustering":
                skill.params["user_metadata"] = input.metadata
                break

    request = {
        "steps": [skill.asdict() for skill in steps],
        "output_type": "json",
        "multilingual": multilingual,
    }
    if include_text:
        request["input"] = input.text
    if csv_params is not None:
        request["csv_params"] = {
            k: v for k, v in csv_params.asdict().items() if v is not None
        }
    if hasattr(input, "type") and input.type:
        request["input_type"] = input.type
    if hasattr(input, "content_type") and input.content_type:
        request["content_type"] = input.content_type
    if hasattr(input, "encoding") and input.encoding:
        request["encoding"] = input.encoding
    return json.dumps(request, default=json_default)


async def post_pipeline(
    session: aiohttp.ClientSession,
    input: Input,
    steps: List[Skill],
    api_key: str,
    multilingual: bool,
    csv_params: CSVParams = None,
) -> Awaitable[Output]:
    validate_api_key(api_key)

    request = build_request(input, steps, multilingual, True, csv_params)
    url = f"{oneai.URL}/{endpoint_default}"
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json",
        "User-Agent": f"python-sdk/{oneai.__version__}/{oneai.api.uuid}",
    }

    if oneai.DEBUG_LOG_REQUESTS:
        oneai.logger.debug(f"POST {url}\n")
        oneai.logger.debug(f"headers={json.dumps(headers, indent=4)}\n")
        oneai.logger.debug(f"data={json.dumps(json.loads(request), indent=4)}\n")

    async with session.post(url, headers=headers, data=request) as response:
        if response.status != 200:
            await handle_unsuccessful_response(response)
        else:
            return build_output(steps, await response.json(), response.headers)


async def post_pipeline_async(
    session: aiohttp.ClientSession,
    input: Input,
    steps: List[Skill],
    api_key: str,
    multilingual: bool,
    csv_params: CSVParams = None,
) -> Awaitable[str]:
    validate_api_key(api_key)

    is_file = isinstance(input.text, io.IOBase)
    endpoint = endpoint_async_file if is_file else endpoint_async
    request = build_request(input, steps, multilingual, not is_file, csv_params)
    endpoint += ("?pipeline=" + urllib.parse.quote(request)) if is_file else ""
    url = f"{oneai.URL}/{endpoint}"
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json",
        "User-Agent": f"python-sdk/{oneai.__version__}/{oneai.api.uuid}",
    }
    data = input.text if is_file else request

    if oneai.DEBUG_LOG_REQUESTS:
        oneai.logger.debug(f"POST {url}\n")
        oneai.logger.debug(f"headers={json.dumps(headers, indent=4)}\n")
        if is_file:
            oneai.logger.debug(
                f"decoded pipeline={json.dumps(json.loads(request), indent=4)}\n"
            )
            oneai.logger.debug(f"data={input.text}\n")
        else:
            oneai.logger.debug(f"data={json.dumps(json.loads(request), indent=4)}\n")

    async with session.post(url, headers=headers, data=data) as response:
        if response.status not in [200, 202]:
            await handle_unsuccessful_response(response)
        else:
            return await response.json()


async def get_task_status(
    session: aiohttp.ClientSession,
    task_id: str,
    api_key: str,
):
    validate_api_key(api_key)

    url = f"{oneai.URL}/{endpoint_async_tasks}/{task_id}"
    headers = {
        "api-key": api_key,
        "User-Agent": f"python-sdk/{oneai.__version__}/{oneai.api.uuid}",
    }

    if oneai.DEBUG_LOG_REQUESTS:
        oneai.logger.debug(f"GET {url}\n")
        oneai.logger.debug(f"headers={json.dumps(headers, indent=4)}\n")

    async with session.get(url, headers=headers) as response:
        if response.status != 200:
            await handle_unsuccessful_response(response)
        else:
            return await response.json()
