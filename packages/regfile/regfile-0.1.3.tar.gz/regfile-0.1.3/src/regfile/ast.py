"""
Abstract Syntax Tree
Added because some thought it was a Good Idea (™) to put json with newlines in
the registry.

The header
The header contains information about what program generated the file.
It's usually
```
Windows Registry Editor Version 5.00
```

The key
A string surrounded by brackets.
This ast DOES NOT differentiate between hives and keys.
Neither does this matter.

The value
This consists of a name
(surronded by double quotation marks)
(or not if it's the default value, which this ast also DOES NOT differentiate between)
and the actual value
(which contents of depend on it's type)
"""
from dataclasses import dataclass, field
from enum import (
    Enum,
    auto,
)
from typing import (
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
)


class Token:
    """Base token class"""


@dataclass
class TComment(Token):
    """
    A comment
    This class is also used to store the header
    """
    text: str


@dataclass
class TValue(Token, Iterable):
    """
    A value
    Only the name relative to the key and the value are stored
    """
    name: str
    value: str

    def __iter__(self):
        return iter([self.name, self.value])


@dataclass
class TKey(Token, Iterable):
    """A key"""
    name: str
    values: List[TValue] = field(default_factory=list)

    def __iter__(self):
        return iter(self.values)

    def append(self, value: TValue):
        """Add a TValue to the key"""
        self.values.append(value)


class AstState(Enum):
    """The state of the ast parser"""
    EXPECT_HEADER = auto()
    HEADER = auto()
    KEY = auto()
    # End of line
    EOL = auto()
    EXPECT_VALUE = auto()
    VALUE_NAME = auto()
    VALUE_VALUE = auto()
    EOF = auto()


@dataclass
class StringCounter(Iterable):
    """Iterable that counts lines/columns"""
    text: str
    cursor: int = 0
    line: int = 1
    column: int = 1

    def __iter__(self) -> Iterator:
        for (index, char) in enumerate(self.text):
            self.cursor = index
            yield char
            if char == "\n":
                self.line += 1
                self.column = 0
            self.column += 1


# TODO: Make this a subclass of typing.Protocol
# but only after Python 3.7 becomes EOL
class SupportsBool:
    """Denotes a value convertible to a boolean"""
    def __bool__(self) -> bool: ...


@dataclass
class RegAst:
    """
    Turns text into tokens
    For more info check the module docs
    """
    textiter: StringCounter
    state: AstState = AstState.EXPECT_HEADER
    default_state: AstState = AstState.EXPECT_HEADER
    currentkey: Optional[TKey] = None
    prevtext: str = ""
    tokens: List[Token] = field(default_factory=list)

    vinfo: Dict[str, str] = field(default_factory=dict)
    quoting_depth: int = 0
    escape_depth: int = 0

    def _function_of_state(self) -> Callable[[str], bool]:
        # NOTE: The returned value is is incorrect
        return getattr(self, f"do_{self.state.name.lower()}")

    def newline(self) -> None:
        """Clear stored text and reset the state"""
        self.prevtext = ""
        self.state = self.default_state


    def do_expect_header(self, char: str) -> bool:
        """
        If the line does not start with an opening bracket then treat the line as a comment.
        Otherwhise expect all following new lines to be a value.
        """
        if char == "[":
            self.default_state = AstState.EXPECT_VALUE
            self.state = AstState.KEY
        if char == "\n":
            token = TComment(self.prevtext)
            self.tokens.append(token)
            self.newline()
            return True
        return False

    def do_header(self, char: str) -> bool:
        """
        Store characters until a newline is encountered.
        Then create a TComment class.
        """
        if char == "\n":
            token = TComment(self.prevtext)
            self.tokens.append(token)
            self.newline()
            return True
        return False

    def do_key(self, char: str) -> None:
        """
        Store characters until a closing bracket is encountered.
        Then create a TKey class.
        """
        if char == "]":
            self.state = AstState.EOL

            name = self.prevtext[1:]
            token = TKey(name)
            self.currentkey = token
            self.tokens.append(token)

    def do_eol(self, char: str) -> bool:
        """Expect no more data until the end of the line."""
        if char == "\n":
            self.newline()
            return True
        return False

    def do_expect_value(self, char: str) -> bool:
        """
        Make sure not previous text is stored, otherwhise something has gone wrong.
        Don't do anything if a newline is encountered.
        If an opening bracket is encountered load a key.
        Otherwhise load a value.
        """
        assert self.prevtext == ""
        if char == "\n":
            self.newline()
            return True
        if char == "[":
            self.state = AstState.KEY
            return False
        if char == "\"":
            self.quoting_depth += 1
        self.state = AstState.VALUE_NAME
        self.vinfo["name"] = char
        self.vinfo["value"] = ""
        return False

    def do_value_name(self, char: str) -> None:
        """
        Store characters until an equal sign is encountered at the end of the value's name.
        """
        if char == "\\":
            self.escape_depth += 1
        if char == "\"":
            if self.quoting_depth <= self.escape_depth:
                self.quoting_depth += 1
            else:
                self.quoting_depth -= 1
        if char == "=" and self.quoting_depth == 0:
            self.state = AstState.VALUE_VALUE
            return
        if char != "\\":
            self.escape_depth = 0
        self.vinfo["name"] += char

    def do_value_value(self, char: str) -> bool:
        """Store characters until a newline is reached"""
        if char == "\\":
            self.escape_depth += 1
        if char == "\n" and self.escape_depth == 0:
            (name, value) = self.vinfo.values()
            token = TValue(name, value)
            assert self.currentkey is not None
            self.currentkey.append(token)
            self.newline()
            return True
        if char != "\\":
            self.escape_depth = 0
        self.vinfo["value"] += char
        return False

    def do_eof(self, _) -> None:
        """
        Do nothing.
        Unused since nothing within the file format denotes the end of a file.
        """
        return

    def _from_str(self) -> List[Token]:
        for char in self.textiter:
            fun = self._function_of_state()
            if not fun(char):
                self.prevtext += char
        assert self.state == AstState.EXPECT_VALUE
        return self.tokens

    @classmethod
    def from_str(cls, text: str) -> List[Token]:
        """
        Turn text into a list of tokens.
        Creates an instance and runs a private method.
        """
        return cls(StringCounter(text))._from_str()
