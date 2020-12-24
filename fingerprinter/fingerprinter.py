"""Main module."""

import collections
from typing import Generator

import bs4
from bs4 import BeautifulSoup


class Fingerprinter:
    def __init__(self, contents):
        soup = bs4.BeautifulSoup(contents, features="html.parser")

        ids = collections.Counter(Fingerprinter.ids(soup))
        classes = collections.Counter(Fingerprinter.classes(soup))

        ids_top3 = ",".join((f"i:{i}" for i, _ in ids.most_common(3)))
        classes_top3 = ",".join(f"c:{c}" for c, _ in classes.most_common(3))

        # calculate tag count
        tag_count = len(list(soup.descendants))

        # calculate fingerprint
        self.fingerprint = f"{ids_top3}+{classes_top3}+{tag_count}"

    @staticmethod
    def classes(soup: BeautifulSoup) -> Generator[str, None, None]:
        """A generator over the classes of all tags."""
        for t in soup.descendants:
            try:
                yield from t['class']
            except (KeyError, TypeError):
                continue

    @staticmethod
    def ids(soup: BeautifulSoup) -> Generator[str, None, None]:
        """A generator over the IDs of all tags."""
        for t in soup.descendants:
            try:
                yield t['id']
            except (KeyError, TypeError):
                continue
