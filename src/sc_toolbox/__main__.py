#!/usr/bin/env python
"""Command-line interface."""
import click
from rich import traceback


@click.command()
@click.version_option()
def main() -> None:
    """sc-toolbox."""


if __name__ == "__main__":
    traceback.install()
    main(prog_name="sc-toolbox")  # pragma: no cover
