"""Console script for fingerprinter."""
import sys

import click

from fingerprinter.fingerprinter import Fingerprinter


@click.command()
@click.argument("files", required=False, nargs=-1)
def main(files):
    """Console script for fingerprinter."""
    if files:
        for file in files:
            contents = open(file, "r")
            print("{} {}".format(file, Fingerprinter(contents).fingerprint))
    else:
        contents = sys.stdin.read()
        print("- {}".format(Fingerprinter(contents).fingerprint))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
