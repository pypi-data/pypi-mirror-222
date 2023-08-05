"""
Parser for .reg files.
"""
# pylint: disable=invalid-name
from __future__ import annotations
import re
from dataclasses import dataclass
from pathlib import Path
from os import (
    PathLike,
    fspath,
)
from typing import (
    ClassVar,
    Optional,
    Sequence,
)

from .ast import (
    TComment,
    TKey,
    RegAst,
)
from .common import REG_ENCODING
from .types import (
    escape,
    RegPath,
    Key,
)


@dataclass
class RegFileHeader:
    version: str
    has_bom: bool = False
    MIME: ClassVar[str] = "Windows Registry Editor Version {}"
    MIME_BOM: ClassVar[str] = "\ufeff"
    MIME_RE: ClassVar[str] = r"Windows Registry Editor Version (.+)"

    @classmethod
    def from_str(cls, data: str) -> "RegFileHeader":
        has_bom: bool = False
        mime = data.split("\n")[0]
        if mime[0] == cls.MIME_BOM:
            mime = mime[1:]
            has_bom = True
        match = re.match(cls.MIME_RE, mime)
        if not match:
            raise TypeError(f"""Not a registry file!
Unknown mime type: {escape(mime)}""")
        version = str(match.groups(0)[0])
        if version != "5.00":
            raise RuntimeError("Unsupported reg file version.")
        return cls(version, has_bom)

    def dump(self) -> str:
        res = self.MIME.format(self.version)
        if self.has_bom:
            res = self.MIME_BOM + res
        return res + "\n"


@dataclass
class RegFile:
    header: RegFileHeader
    keys: list[Key]
    root_key: Optional[RegPath]

    @classmethod
    def from_str(cls, data: str) -> "RegFile":
        tokens = RegAst.from_str(data)
        keys: list[Key] = []
        header_str = ""
        header: Optional[RegFileHeader] = None
        root_key: Optional[Key] = None
        for token in tokens:
            if isinstance(token, TComment):
                header_str += token.text + "\n"
            elif isinstance(token, TKey):
                key = Key.from_token(token)
                if key.parent is None:
                    keys.append(key)
                    continue
                if not keys:
                    # Otherwhise it's a partial reg file
                    if not root_key:
                        root_key = key
                        continue
                    if len(key.parent) == len(root_key.path):
                        root_key.add_subkey(key)
                        continue
                parent_found = False
                root_keys = keys.copy()
                if root_key:
                    root_keys += [root_key]
                for sub_root_key in root_keys:
                    srk_path = sub_root_key.path
                    if not key.parent.startswith(srk_path):
                        continue
                    parent_key = sub_root_key.find_key(key.parent.path)
                    parent_key.add_subkey(key)
                    parent_found = True
                    break
                if parent_found:
                    continue
                raise ValueError(f"{escape(key.name)}'s parent not found'")
        header = RegFileHeader.from_str(header_str)
        # Add missing keys
        root_path = None
        if root_key:
            tmp = root_key
            tmp_parent: Key
            while tmp.parent:
                tmp_parent = Key(tmp.parent)
                tmp_parent.add_subkey(tmp)
                tmp = tmp_parent
            keys.append(tmp)
            root_path = root_key.path
        return cls(header, keys, root_path)

    @classmethod
    def from_path(cls, path: PathLike):
        path = Path(fspath(path))
        return cls.from_str(path.read_text(REG_ENCODING))

    def __getitem__(self, name: str) -> Key:
        for key in self.keys:
            if key.name == name:
                return key
        raise KeyError(name)

    def find_key(self, path: RegPath | Sequence[str] | str) -> Key:
        """
        Finds key by path.
        """
        if isinstance(path, RegPath):
            path = path.path
        if isinstance(path, str):
            path = path.split("\\")
        search = path[0]
        key = self[search]
        return key.find_key(path)

    @property
    def HKEY_CLASSES_ROOT(self) -> Key:
        return self["HKEY_CLASSES_ROOT"]

    @property
    def HKEY_CURRENT_USER(self) -> Key:
        return self["HKEY_CURRENT_USER"]

    @property
    def HKEY_LOCAL_MACHINE(self) -> Key:
        return self["HKEY_LOCAL_MACHINE"]

    @property
    def HKEY_USERS(self) -> Key:
        return self["HKEY_USERS"]

    @property
    def HKEY_CURRENT_CONFIG(self) -> Key:
        return self["HKEY_CURRENT_CONFIG"]

    def dump(self) -> str:
        """
        Dump registry file to string.
        Remember that Windows's reg files use CRLF as line endings.

        Returns:
            str: Registry file as string.
        """

        res = self.header.dump() + "\n"
        if self.root_key is not None:
            root = self.find_key(str(self.root_key))
            assert root is not None
            keys = [root]
        else:
            keys = self.keys
        all_keys = []
        while keys:
            key = keys.pop(0)
            all_keys.append(key)
            keys = key.subkeys + keys
        while len(all_keys) > 0:
            key = all_keys.pop(0)
            res += key.dump()
        return res
