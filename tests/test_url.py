import threading
import unittest
from typing import List

from crawler.url import URL, ResourceType


class URLTests(unittest.TestCase):
    def test_basic(self):
        test_url = "https://skunichetty.dev/posts/a-very-cool-post/hidden-url/"
        parsed = URL(test_url)
        assert parsed.scheme == "https"
        assert parsed.type == ResourceType.FOLDER
        assert parsed.path == "/posts/a-very-cool-post/hidden-url/"

    def test_partial_url(self):
        test_url = "/posts/a-very-cool-post/hidden-url/"
        parsed = URL(test_url)
        assert parsed.scheme == ""
        assert parsed.location == ""
        assert parsed.type == ResourceType.FOLDER
        assert parsed.path == "/posts/a-very-cool-post/hidden-url/"

    def test_join(self):
        base = URL("https://skunichetty.dev/subdir/")
        urls = [
            ("https://skunichetty.dev/otherdir/", "https://skunichetty.dev/otherdir/"),
            ("/otherdir/", "https://skunichetty.dev/otherdir/"),
            ("otherdir/", "https://skunichetty.dev/subdir/otherdir/"),
            ("../otherdir/", "https://skunichetty.dev/otherdir/"),
        ]

        for input, output in urls:
            assert base.join(URL(input)) == URL(output)

    def test_join_no_trailing(self):
        base = URL("https://skunichetty.dev/subdir/subsubdir")
        urls = [
            ("https://skunichetty.dev/otherdir/", "https://skunichetty.dev/otherdir/"),
            ("/otherdir/", "https://skunichetty.dev/otherdir/"),
            ("otherdir/", "https://skunichetty.dev/subdir/otherdir/"),
            ("../otherdir/", "https://skunichetty.dev/otherdir/"),
        ]

        for input, output in urls:
            joined = base.join(URL(input))
            assert joined == URL(output), f"{joined} != {output}"

    def test_hash(self):
        url1 = URL("https://skunichetty.dev/item1/")
        url2 = URL("https://skunichetty.dev/item1/")
        urls = set([url1, url2])
        assert len(urls) == 1

    def test_resource_type(self):
        urls = [
            ("https://skunichetty.dev/index.html", ResourceType.FILE),
            ("https://skunichetty.dev/", ResourceType.FOLDER),
            ("https://skunichetty.dev/index", ResourceType.FILE),
            ("https://skunichetty.dev/index/", ResourceType.FOLDER),
        ]
        for input, output in urls:
            inferred_type = ResourceType.from_url(input)
            assert (
                inferred_type == output
            ), f"{input} inferred to be {inferred_type} != {output}"
