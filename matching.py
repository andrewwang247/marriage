"""
Stable Marriage Problem solution using Gale-Shapley.

Copyright 2020. Siwei Wang.
"""
# pylint: disable=no-value-for-parameter
from typing import Union
import click
from read_validate import get_smp
from marriage import compute_smp
from write import print_results


@click.command()
@click.option('--filename', '-f', required=True,
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              help='Path to input json on which to run SMP algorithm.')
@click.option('--output', '-o', required=False,
              type=click.Path(exists=False, file_okay=True, dir_okay=False),
              help='Path to output file in which to print results.')
def main(filename: str, output: Union[str, None]):
    """Execute smp algorithm on input and print results to output."""
    men_pref, women_pref = get_smp(filename)
    men_engage, women_engage = compute_smp(men_pref, women_pref)
    print_results(men_engage, women_engage, output)


if __name__ == '__main__':
    main()
