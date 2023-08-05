import csv
import datetime
import logging
import logging.config
import sys
from dataclasses import asdict, fields
from typing import Annotated, Final

import pkg_resources
import typer

from iscwatch.advisory import Advisory
from iscwatch.logconfig import logging_config
from iscwatch.scrape import iter_advisories

logging.config.dictConfig(logging_config)

PACKAGE_NAME: Final = "iscwatch"


def cli():
    """CLI entry point executes typer-wrapped main function"""
    typer.run(main)


def main(
    since: Annotated[
        datetime.datetime,
        typer.Option(
            "--since", "-s", help="Exclude summaries before date.", formats=["%Y-%m-%d"]
        ),
    ] = datetime.datetime.min,
    version: Annotated[
        bool,
        typer.Option("--version", "-v", help="Output product version and exit."),
    ] = False,
    no_headers: Annotated[
        bool,
        typer.Option("--no-headers", "-n", help="Omit column headers from CSV output."),
    ] = False,
    last_updated: Annotated[
        bool,
        typer.Option("--last-updated", "-l", help="Output date when last updated and exit."),
    ] = False,
):
    """Disposition command line and vector work to appropriate sub-function."""
    if version:
        print_version()
    elif last_updated:
        last_updated_advisory = max(iter_advisories(), key=lambda a: a.updated)
        print(last_updated_advisory.updated)
    else:  # output advisories
        selected_advisories = [
            a for a in iter_advisories() if not since or a.updated >= since.date()
        ]
        print_csv_advisories(selected_advisories, no_headers)


def print_csv_advisories(advisories: list[Advisory], no_headers: bool):
    """Convert advisories into dictionaries and output in CSV format."""
    fieldnames = [field.name for field in fields(Advisory)]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    if not no_headers:
        writer.writeheader()
    writer.writerows(asdict(advisory) for advisory in advisories)


def print_version():
    """Output current version of the application."""
    try:
        distribution = pkg_resources.get_distribution(PACKAGE_NAME)
        print(f"{distribution.project_name} {distribution.version}")
    except pkg_resources.DistributionNotFound:
        logging.error(f"The package ({PACKAGE_NAME}) is not installed.")
