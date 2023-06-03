import re
from enum import Enum


class RegexPattern:
    HTML = re.compile(r"\.html$")
    BASE = re.compile(r"^https?\:\/\/")
    NORM = re.compile(r"[^\w\d\/\_\-]")
    NORM_HTML = re.compile(r"[^\w\d\/\_\-\.]")
    STRIPBASE = re.compile(r"\/\w+\.\w+$")
    TRAILING_SLASH = re.compile("\/$")


class NodeType(int, Enum):
    INTERNAL = 0
    WEBPAGE = 1


def normalize_url(url: str):
    # want to strip all dots except for .html
    url = RegexPattern.TRAILING_SLASH.sub("", url)
    url = RegexPattern.BASE.sub("", url)  # remove https
    if RegexPattern.HTML.search(url):
        filter = RegexPattern.NORM_HTML
    else:
        filter = RegexPattern.NORM
    url = filter.sub("_", url)
    return url
