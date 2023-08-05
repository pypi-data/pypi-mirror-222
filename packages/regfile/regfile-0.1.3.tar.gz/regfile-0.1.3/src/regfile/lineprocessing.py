"""
Line processing
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
import re
from typing import (
    Optional,
    Tuple,
    Type,
)
from .ast import TValue


NVPair = Tuple[str, str]


def linelimit(line: str, limit: int = 80) -> str:
    """
    Limit a line to a certain length by adding newlines after some commas.

    >>> linelimit("aa,bb,cc,dd", limit=6)
    'aa,bb,\\ncc,dd'
    >>> linelimit('abc=01,23,45,67,89,ab,cd,ef', limit=16)
    'abc=01,23,45,\\n  67,89,ab,cd,\\n  ef'
    >>> linelimit('aaaaaaaaaa=01,23,45,67,89,ab,cd,ef', limit=10)
    'aaaaaaaaaa=01,\\n  23,45,\\n  67,89,\\n  ab,cd,\\n  ef'

    Args:
        line: The line to limit.
        limit: The maximum length of the line.

    Returns:
        The line, limited to the given length.
    """
    if "," not in line:
        return line
    res = ""
    char_count = 0
    for chars in line.split(","):
        added_chars = chars + ","
        res += added_chars
        char_count += len(added_chars)
        if char_count + len(chars) > limit - 2:
            res += "\\\n  "
            char_count = 2
    if res.endswith(","):
        res = res[:-1]
    return res


def text_to_nvpair(text: str) -> NVPair:
    # TODO: Find a better way to do this
    equal_sign_index = 0
    quoting_depth = 0
    escape_depth = 0
    for char in text:
        equal_sign_index += 1
        if char == "\\":
            escape_depth += 1
        if char == "\"":
            if quoting_depth <= escape_depth:
                quoting_depth += 1
            else:
                quoting_depth -= 1
        if char == "=" and quoting_depth == 0:
            break
        escape_depth = 0
    return (
        text[:equal_sign_index - 1],
        text[equal_sign_index:]
    )


@dataclass(init=True)
class NVLine(TValue):
    "Name-Value line"
    processor: Optional[Type[LineProcessor]] = None

    @property
    def is_processed(self) -> bool:
        return not self.process

    @classmethod
    def from_str(
        cls,
        text: str
    ) -> "NVLine":
        name: str
        value: str
        if len(list(re.finditer("=", text))) == 1:
            name = text.split("=")[0]
            value = text[len(name) + 1:]
        else:
            (name, value) = text_to_nvpair(text)
        return cls(name, value)

    def process(self, processor: Type[LineProcessor]) -> None:
        self.processor = processor
        (self.name, self.value) = processor.preprocess(
            (self.name, self.value)
        )

    def deprocess(self) -> None:
        if not self.processor:
            raise RuntimeError("Attemting to deprocess a non-processed value")
        (self.name, self.value) = self.processor.postprocess(
            (self.name, self.value)
        )
        self.processor = None

    def to_str(self) -> str:
        return f"{self.name}={self.value}"


class LineProcessor(ABC):
    """
    Abstract base class for line processing.
    """
    @staticmethod
    @abstractmethod
    def preprocess(line: NVPair) -> NVPair:
        """
        Preprocess a line.

        Args:
            line: The line to preprocess.

        Returns:
            The preprocessed text.
        """
    @staticmethod
    @abstractmethod
    def postprocess(line: NVPair) -> NVPair:
        """
        Postprocess a line.

        Args:
            line: The line to postprocess.

        Returns:
            The postprocessed line.
        """


class LPNone(LineProcessor):
    """
    Post-processor that does nothing.
    """
    @staticmethod
    def preprocess(line: NVPair) -> NVPair:
        "Returns the line as is"
        return line

    @staticmethod
    def postprocess(line: NVPair) -> NVPair:
        "Returns the line as is"
        return line


class LPLinelimit(LineProcessor):
    """
    Post-processor that limits a line to ~80 characters.
    """
    @staticmethod
    def preprocess(line: NVPair) -> NVPair:
        "Returns the line as is"
        (name, value) = line
        return (name, value.replace("\\\n  ", ""))

    @staticmethod
    def postprocess(line: NVPair) -> NVPair:
        "Limits the line to ~80 characters"
        name = line[0]
        strline = "=".join(line)
        limited_value = linelimit(strline)[len(name) + 1:]
        return (name, limited_value)
