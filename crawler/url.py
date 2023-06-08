from urllib.parse import urlparse, urljoin, urlunparse
from enum import Enum
import re

EXT_PATTERN = re.compile(r"\/[^\.\/]+(?:\.([\w\d]+))?$")


class ResourceType(str, Enum):
    """Type of the resource located at some server endpoint."""

    FILE = "file"
    FOLDER = "folder"

    @staticmethod
    def from_url(path: str) -> "ResourceType":
        search_result: re.Match = EXT_PATTERN.search(path)
        try:
            _ = search_result[1]  # try to access the second group
            return ResourceType.FILE
        except TypeError:
            return ResourceType.FOLDER


class URL:
    """OOP abstraction of a url"""

    def __init__(self, url: str) -> None:
        self.scheme, self.location, self.path, _, _, _ = urlparse(url)
        # reparse to remove redundant delimiters based on RFC
        self._url_string = urlunparse(
            (self.scheme, self.location, self.path, "", "", "")
        )
        self.type = ResourceType.from_url(self.path)

    def __str__(self) -> str:
        # TODO: Profile memory impact of storing actual string
        return self._url_string

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash((self.scheme, self.location, self.path))

    def __eq__(self, rhs: "URL") -> bool:
        return (
            self.scheme == rhs.scheme
            and self.location == rhs.location
            and self.path == rhs.path
        )

    def join(self, rhs: "URL") -> "URL":
        return URL(urljoin(self._url_string, rhs._url_string))
