from datetime import datetime, timedelta
from dateutil import parser as dateutil
import io
import os
from base64 import b64encode
import validators
from dataclasses import dataclass, field
from typing import (
    Any,
    BinaryIO,
    Dict,
    Generic,
    List,
    Optional,
    TextIO,
    Tuple,
    TypeVar,
    Union,
)
from typing_extensions import dataclass_transform, Literal
from warnings import warn

from oneai.exceptions import InputError


@dataclass
class Utterance:
    speaker: str
    utterance: str
    timestamp: Optional[timedelta] = None

    @classmethod
    def from_dict(cls, u: Dict[str, str]) -> "Utterance":
        return cls(
            u.get("speaker", None),
            u["utterance"],
            timestamp_to_timedelta(u.get("timestamp", None)),
        )

    def __repr__(self) -> str:
        return (
            f"\n\t{self.timestamp} {self.speaker}: {self.utterance}"
            if self.timestamp
            else f"\n\t{self.speaker}: {self.utterance}"
            if self.speaker
            else f"\n\t{self.utterance}"
        )


TextContent = TypeVar("TextContent", bound=Union[str, List["Utterance"]])
PipelineInput = Union["Input[TextContent]", TextContent, TextIO, BinaryIO]

# extension -> content_type, input_type
CONTENT_TYPES: Dict[str, Tuple[str, str]] = {
    ".json": ("application/json", "conversation"),
    ".txt": ("text/plain", "article"),
    ".srt": ("text/plain", "conversation"),
    ".wav": ("audio/wav", "conversation"),
    ".mp3": ("audio/mpeg", "conversation"),
    ".mp4": ("audio/mpeg", "conversation"),
    ".html": ("text/plain", "article"),
    ".pdf": ("text/pdf", "article"),
    ".csv": ("text/csv", "article"),
}


@dataclass(frozen=True)
class Skill:
    """
    A base class for all Language Skills. Use predefined subclasses of this class, or use this class to define your own Skills.

    A Language Skill is a package of trained NLP models. Skills accept text and respond with processed texts and extracted metadata.

    Process texts with Skills using `Pipeline`s

    ### Skill types
    * Generator Skills (`text_attr is not None`) process the input and produce a new text based on it. Examples include `Summarize`, `Proofread`.
    * Analyzer Skills (`text_attr is None`) scan the input and extract structured data. Examples include `Emotions`, `Topics`.

    ## Attributes

    `api_name: str`
        The name of the Skill in the pipeline API.
    `text_attr: str`
        The attribute name of the Skill's output text in the Output object (Generator Skills only).
    `labels_attr: str`
        The attribute name of the Skill's output labels in the Output object.
    `params: dict[str, Any]`
        The parameters of the Skill. See the documentation for each Skill for a list of available parameters.
    """

    api_name: str = ""
    text_attr: Optional[str] = None
    labels_attr: Optional[str] = None
    params: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        # backwards compatibility
        if self.labels_attr is None and self.text_attr is None:
            object.__setattr__(self, "labels_attr", self.api_name)

    def asdict(self) -> dict:
        return {
            "skill": self.api_name,
            "params": {k: v for k, v in self.params.items() if v is not None},
        }


@dataclass_transform()
def skillclass(
    api_name: str = "",
    text_attr: Optional[str] = None,
    labels_attr: Optional[str] = None,
):
    """
    A decorator for defining a Language Skill class. Decorate subclasses of `Skill` with this to provide default values for instance attributes.

    ## Example

    >>> @skillclass(api_name="my-skill", text_attr="my_result")
    ... class MySkill(Skill):
    ...     ratio: float = 0.2
    >>> s = Summarize(ratio=0.5)
    >>> s.ratio
    0.5
    >>> pipeline = Pipeline([s])
    >>> output = pipeline.run("Text to be processed with MySkill")
    >>> output.my_result
    "Result text, processed with MySkill"
    """

    def wrap(cls):
        if not issubclass(cls, Skill):
            warn(
                f"warning: class {cls.__name__} decorated with @skillclass does not inherit Skill",
                stacklevel=2,
            )

        # remove class variables
        classVars = {
            k: getattr(cls, k, None)
            for k in cls.__annotations__
            if k not in Skill.__annotations__
        }
        for k in classVars:
            if hasattr(cls, k):
                delattr(cls, k)

        def __init__(self, **params):
            if "params" in params and isinstance(params["params"], dict):
                params = {**params, **params["params"]}
                del params["params"]

            Skill.__init__(
                self,
                api_name=params.pop("api_name", api_name),
                text_attr=params.pop("text_attr", text_attr),
                labels_attr=params.pop("labels_attr", labels_attr),
                params=params,
            )

            for k, v in classVars.items():
                if k not in self.params and k is not None:
                    self.params[k] = v

        def __getattr__(self, name):
            if name in Skill.__annotations__:
                return object.__getattribute__(self, name)

            if name not in classVars:
                raise AttributeError(
                    f"'{self.__class__.__name__}' object has no attribute '{name}'"
                )
            return self.params.get(name, None)

        def __setattr__(self, name, value):
            if name in Skill.__annotations__:
                return object.__setattr__(self, name, value)

            if name not in classVars:
                warn(
                    f"warning: parameter '{name}' not defined in class {self.__class__.__name__}",
                    stacklevel=2,
                )
            self.params[name] = value

        cls.__init__ = __init__
        cls.__getattr__ = __getattr__
        cls.__setattr__ = __setattr__
        return cls

    return wrap


class Input(Generic[TextContent]):
    """
    A base class for all input texts, allowing structured representations of inputs.

    ## Attributes

    `text: TextContent`
        Input text. Either `str` or `list[Utterance]` (conversation).
    `type: str`
        A type hint for the API, suggesting which models to use when processing the input.
    `content_type: str`
        The content type of the input.
    `encoding: str`
        The encoding of the input.
    `metadata: dict`
        Optional metadata to be associated with the input in clustering collections.
    `datetime: datetime`
        Optional datetime to be associated with the input in clustering collections.
    `text_index: str`
        Optional text index to be associated with the input in clustering collections.
    """

    def __init__(
        self,
        text: TextContent,
        *,
        type: str = None,
        content_type: str = None,
        encoding: str = None,
        metadata: Dict[str, any] = None,
        datetime: datetime = None,
        text_index: str = None,
    ):
        self.text: TextContent = text
        self.type = type
        self.content_type = content_type
        self.encoding = encoding
        self.metadata = metadata
        self.datetime = datetime
        self.text_index = text_index

    @classmethod
    def wrap(
        cls,
        text: PipelineInput[TextContent],
    ) -> "Input[TextContent]":
        if isinstance(text, cls):
            return text
        elif isinstance(text, str):
            if validators.url(text):
                return cls(text, type="article", content_type="text/uri-list")
            else:
                return cls(text, type="article", content_type="text/plain")
        elif isinstance(text, list) and (
            len(text) == 0 or isinstance(text[0], Utterance)
        ):
            return cls(text, type="conversation", content_type="application/json")
        elif isinstance(text, io.IOBase):
            _, ext = os.path.splitext(text.name)
            if ext not in CONTENT_TYPES:
                raise InputError(
                    message=f"unsupported file extension {ext}",
                    details="see supported files in docs",
                )
            content_type, input_type = CONTENT_TYPES[ext]
            if ext == ".csv" and isinstance(text, io.TextIOBase):
                text = io.BytesIO(text.read().encode("utf-8"))
            return cls(text, type=input_type, content_type=content_type)
        else:
            raise ValueError(f"invalid content type {type(text)}")

    def _make_sync(self) -> "Input[Union[str, List[Utterance]]]":
        if isinstance(self.text, io.BufferedIOBase):
            self.text = b64encode(self.text.read()).decode("ascii")
            self.encoding = "base64"
        elif isinstance(self.text, io.TextIOBase):
            self.text = self.text.read()
        return self


def timestamp_to_timedelta(timestamp: str) -> timedelta:
    if not timestamp:
        return None
    try:
        dt = dateutil.parse(timestamp)
    except Exception as e:
        warn("Received invalid timestamp: {}, returning as str".format(timestamp))
        return timestamp
    return timedelta(
        hours=dt.hour, minutes=dt.minute, seconds=dt.second, microseconds=dt.microsecond
    )


@dataclass
class Span:
    start: int
    end: int
    section: int = 0
    text: str = None

    @classmethod
    def from_dict(cls, objects: List[dict], text: str) -> "List[Span]":
        return (
            []
            if not objects
            else [
                cls(
                    start=object.get("start", None),
                    end=object.get("end", None),
                    section=object.get("section", None),
                    text=text,
                )
                for object in objects
            ]
        )


@dataclass
class Label:
    """
    Represents a label, marking a part of the input text. Attribute values largely depend on the Skill the labels were produced by.

    ## Attributes

    `type: str`
        Label type, e.g. 'entity', 'topic', 'emotion'.
    `skill: str`
        The name of the Skill that produced the label.
    `name: str`
        Label class name, e.g. 'PERSON', 'happiness', 'POS'.
    `output_spans: list[Span]`
        The spans in the output text that are marked with the label.
    `input_spans: list[Span]`
        The spans in the input text that are relevant to the label. Only appears if the label was produced by a Skill that supports input spans.
    `span_text: str`
        The text of the label.
    `timestamp: str`
        For audio inputs, the timestamp of the start of the label.
    `timestamp_end: str`
        For audio inputs, the timestamp of the end of the label.
    `value: str`
        The value of the label.
    `data: Dict[str, Any]`
        Additional data associated with the label.
    """

    type: str = ""
    skill: str = ""
    name: str = ""
    _span: List[int] = field(default_factory=lambda: [0, 0], repr=False)
    output_spans: List[Span] = field(default_factory=list)
    input_spans: List[Span] = field(default_factory=list)
    span_text: str = ""
    timestamp: timedelta = None
    timestamp_end: timedelta = None
    value: str = ""
    data: dict = field(default_factory=dict)

    @property
    def span(self) -> Span:
        warn(
            "`Label.span` is deprecated, use `Label.output_spans` instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._span

    @classmethod
    def from_dict(cls, object: dict) -> "Label":
        return cls(
            type=object.pop("type", ""),
            skill=object.pop("skill", ""),
            name=object.pop("name", ""),
            output_spans=Span.from_dict(
                object.pop("output_spans", []), object.get("span_text", None)
            ),
            input_spans=Span.from_dict(
                object.pop("input_spans", []), object.get("span_text", None)
            ),
            _span=object.pop("span", [0, 0]),
            span_text=object.pop("span_text", ""),
            value=object.pop("value", ""),
            data=object.pop("data", {}),
            timestamp=timestamp_to_timedelta(object.pop("timestamp", "")),
            timestamp_end=timestamp_to_timedelta(object.pop("timestamp_end", "")),
        )

    def __repr__(self) -> str:
        return (
            "oneai.Label("
            + ", ".join(
                f"{k}={repr(v)}"
                for k, v in self.__dict__.items()
                if v and not k.startswith("_")
            )
            + ")"
        )


class Labels(List[Label]):
    """
    Wrapper object for a list of `Label` objects. Provides convenience methods to query labels by attribute.

    ## Properties

    `values: list[str]`
        A list of all values of the labels.
    `names: list[str]`
        A list of all names of the labels.
    `input_spans: list[list[Span]]`
        A list of all input spans of the labels.
    `output_spans: list[list[Span]]`
        A list of all output spans of the labels.
    `span_texts: list[str]`
        A list of all span texts of the labels.
    """

    @property
    def values(self) -> List[Any]:
        return [l.value for l in self]

    @property
    def names(self) -> List[str]:
        return [l.name for l in self]

    @property
    def input_spans(self) -> List[List[Span]]:
        return [l.input_spans for l in self]

    @property
    def output_spans(self) -> List[List[Span]]:
        return [l.output_spans for l in self]

    @property
    def span_texts(self) -> List[str]:
        return [l.span_text for l in self]


CSVColumn = Union[
    Literal[
        # The text input to be processed
        "input",
        # Input timestamp
        "timestamp",
        # Input translation
        "input_translated",
        # Skip column
        False,
    ],
    # Custom Metadata
    str,
]


@dataclass
class CSVParams:
    columns: List[CSVColumn]
    skip_rows: int = 0
    max_rows: Optional[int] = None

    def asdict(self) -> dict:
        return {
            "columns": self.columns,
            "skip_rows": self.skip_rows,
            "max_rows": self.max_rows,
        }
