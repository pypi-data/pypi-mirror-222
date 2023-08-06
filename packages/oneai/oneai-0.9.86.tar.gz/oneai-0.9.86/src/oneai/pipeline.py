import asyncio
import concurrent.futures
import os
import sys
from typing import Awaitable, Callable, Iterable, List, Union

import oneai
from oneai.classes import (
    PipelineInput,
    Skill,
    TextContent,
    CSVParams,
    Input,
)
from oneai.output import Output, BatchResponse
from oneai.process_scheduler import (
    process_single_input,
    process_single_input_async,
    process_batch,
    task_polling,
)


class Pipeline:
    """
    Language AI pipelines allow invoking and chaining multiple Language Skills to process your input text with a single API call.

    ## Attributes

    `steps: list[Skill]`
        A list of Language Skills to process the input text. The order of the skills in the list determines their input.
    `api_key: str, optional`
        An API key to be used in this pipelines `run` calls. If not provided, the global `oneai.api_key` is used.
    `multilingual: bool, optional`
        Whether the pipeline should be allowed to process multilingual input.

    ## Methods

    `run(input, api_key=None) -> Output`
        Runs the pipeline on the input text.
    `run_async(input, api_key=None) -> Awaitable[Output]`
        Runs the pipeline on the input text asynchronously.
    `run_batch(batch, api_key=None) -> Dict[Input, Output]`
        Runs the pipeline on a batch of input texts.
    `run_batch_async(batch, api_key=None) -> Awaitable[Dict[Input, Output]]`
        Runs the pipeline on a batch of input texts asynchronously.

    ## Pipeline Ordering

    The order of the skills in the pipeline determines their input:
    * Skills that are placed after a generator Skill will receive its output as input.
    * If there's no preceding generator Skill, the original input text is used.

    ## Example

    >>> my_text = 'ENTER-YOUR-TEXT-HERE'
    >>> pipeline = oneai.Pipeline(steps=[
    ...     oneai.skills.Topics(),
    ...     oneai.skills.Summarize(min_length=20),
    ...     oneai.skills.Entities()
    ... ])
    >>> output = pipeline.run(my_text)
    >>> output.topics
    [oneai.Label(type=topic, span=[0, 10], name=topic1), ...] # topics from my_text
    >>> output.summary.text
    '...' # summary of my_text
    >>> output.summary.entities
    [oneai.Label(type=entity, span=[0, 10], name=entity1), ...] # entities from the summary
    """

    def __init__(
        self, steps: List[Skill], api_key: str = None, multilingual: bool = False
    ) -> None:
        self.steps = tuple(steps)  # todo: validate (based on input_type)
        self.api_key = api_key
        self.multilingual = multilingual

    def run(
        self,
        input: PipelineInput[TextContent],
        api_key: str = None,
        multilingual: bool = False,
        *,
        csv_params: CSVParams = None,
    ) -> Output[TextContent]:
        """
        Runs the pipeline on the input text.

        ## Parameters

        `input: PipelineInput`
            The input text to be processed.
        `api_key: str, optional`
            An API key to be used in this API call. If not provided, `self.api_key` is used.

        ## Returns

        An `Output` object containing the results of the Skills in the pipeline.

        ## Raises

        `InputError` if the input is is invalid or is of an incompatible type for the pipeline.
        `APIKeyError` if the API key is invalid, expired, or missing quota.
        `ServerError` if an internal server error occured.
        """
        input = Input.wrap(input)
        return _async_run_nested(
            process_single_input(
                input,
                self.steps,
                api_key or self.api_key or oneai.api_key,
                multilingual or self.multilingual or oneai.multilingual,
                csv_params=csv_params,
            )
        )

    async def run_async(
        self,
        input: PipelineInput[TextContent],
        api_key: str = None,
        interval: int = 1,
        multilingual: bool = False,
        *,
        csv_params: CSVParams = None,
        polling: bool = True,
    ) -> Awaitable[Output[TextContent]]:
        """
        Runs the pipeline on the input text asynchronously.

        ## Parameters

        `input: PipelineInput`
            The input text (or multiple input texts) to be processed.
        `api_key: str, optional`
            An API key to be used in this API call. If not provided, `self.api_key` is used.
        `interval: int, optional`
            The number of seconds to wait between polling for results.
        `polling: bool, optional`
            Whether to poll for results. If `False`, will return an `Output` object with a `task_id`, and `None` for the rest of the fields.

        ## Returns

        An Awaitable with an `Output` object containing the results of the Skills in the pipeline.

        ## Raises

        `InputError` if the input is is invalid or is of an incompatible type for the pipeline.
        `APIKeyError` if the API key is invalid, expired, or missing quota.
        `ServerError` if an internal server error occured.
        """
        input = Input.wrap(input)
        return await process_single_input_async(
            input,
            self.steps,
            api_key or self.api_key or oneai.api_key,
            interval,
            multilingual or self.multilingual or oneai.multilingual,
            csv_params=csv_params,
            polling=polling,
        )

    async def await_completion(
        self,
        task: Union[str, Output],
        api_key: str = None,
        interval: int = 1,
    ) -> Awaitable[Output[TextContent]]:
        if isinstance(task, Output):
            task = task.task_id
        return await task_polling(
            task,
            None,
            api_key or self.api_key or oneai.api_key,
            self.steps,
            interval,
        )

    def run_batch(
        self,
        batch: Iterable[PipelineInput[TextContent]],
        api_key: str = None,
        on_output: Callable[
            [PipelineInput[TextContent], Output[TextContent]], None
        ] = None,
        on_error: Callable[[PipelineInput[TextContent], Exception], None] = None,
        multilingual: bool = False,
    ) -> BatchResponse:
        """
        Runs the pipeline on a batch of input texts.

        ## Parameters

        `batch: Iterable[PipelineInput]`
            The input texts to be processed.
        `api_key: str, optional`
            An API key to be used in this API call. If not provided, `self.api_key` is used.
        `on_output: Callable[[Input, Output], None]`
            Action to perform on successful output, by default creates a dict mapping inputs to outputs
        `on_error: Callable[[Input, Exception], None]`
            Action to perform on error, by default creates a dict mapping inputs to errors

        ## Returns

        Unless on_output/on_error are modified, returns a dictionary mapping inputs to the produced `Output` objects, each containing the results of the Skills in the pipeline.

        ## Raises

        `InputError` if the input is is invalid or is of an incompatible type for the pipeline.
        `APIKeyError` if the API key is invalid, expired, or missing quota.
        `ServerError` if an internal server error occured.
        """
        return _async_run_nested(
            self.run_batch_async(batch, api_key, on_output, on_error, multilingual)
        )

    async def run_batch_async(
        self,
        batch: Iterable[PipelineInput[TextContent]],
        api_key: str = None,
        on_output: Callable[
            [PipelineInput[TextContent], Output[TextContent]], None
        ] = None,
        on_error: Callable[[PipelineInput[TextContent], Exception], None] = None,
        multilingual: bool = False,
    ) -> Awaitable[BatchResponse]:
        """
        Runs the pipeline on a batch of input texts asynchronously.

        ## Parameters

        `batch: Iterable[str | Input]`
            The input texts to be processed.
        `api_key: str, optional`
            An API key to be used in this API call. If not provided, `self.api_key` is used.
        `on_output: Callable[[Input, Output], None]`
            Action to perform on successful output, by default creates a dict mapping inputs to outputs
        `on_error: Callable[[Input, Exception], None]`
            Action to perform on error, by default creates a dict mapping inputs to errors

        ## Returns

        Unless on_output/on_error are modified, returns an Awaitable with a dictionary mapping inputs to the produced `Output` objects, each containing the results of the Skills in the pipeline.

        ## Raises

        `InputError` if the input is is invalid or is of an incompatible type for the pipeline.
        `APIKeyError` if the API key is invalid, expired, or missing quota.
        `ServerError` if an internal server error occured.
        """
        outputs = BatchResponse()
        await process_batch(
            (Input.wrap(i) for i in batch),
            self.steps,
            on_output if on_output else outputs.__setitem__,
            on_error if on_error else outputs.__setitem__,
            api_key=api_key or self.api_key or oneai.api_key,
            multilingual=multilingual or self.multilingual or oneai.multilingual,
        )
        return outputs

    def __repr__(self) -> str:
        return f"oneai.Pipeline({self.steps})"


# for jupyter environment, to avoid "asyncio.run() cannot be called from a running event loop"
pool = concurrent.futures.ThreadPoolExecutor()
is_36 = sys.version_info[:2] == (3, 6)

if os.name == "nt" and not is_36:  # Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def _async_run_nested(coru):
    if is_36:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(coru)
    else:
        try:
            asyncio.get_running_loop()
            return pool.submit(asyncio.run, coru).result()
        except RuntimeError:
            pass

        return asyncio.run(coru)
