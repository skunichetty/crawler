# web crawler
import logging
import pathlib

import click

from scraper.crawl import crawl

logger = logging.getLogger(__name__)


@click.command("Crawler")
@click.argument("url")
@click.argument("storage_directory")
def main(url: str, storage_directory: str):
    crawl(url, pathlib.Path(storage_directory))


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    main()
