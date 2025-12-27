"""
Stable Marriage Problem solution using Gale-Shapley.

Copyright 2026. Andrew Wang.
"""
# pylint: disable=no-value-for-parameter
from typing import Optional
from click import command, option, Path
from read_validate import get_smp
from marriage import compute_smp
from write import print_results


@command()
@option('--filename', '-f', required=True,
        type=Path(exists=True, file_okay=True, dir_okay=False),
        help='Path to input json on which to run SMP algorithm.')
@option('--output', '-o', required=False,
        type=Path(exists=False, file_okay=True, dir_okay=False),
        help='Path to output file in which to print results.')
def main(filename: str, output: Optional[str]):
    """Execute smp algorithm on input and print results to output."""
    men_pref, women_pref = get_smp(filename)
    men_engage, women_engage = compute_smp(men_pref, women_pref)
    print_results(men_engage, women_engage, output)


if __name__ == '__main__':
    main()
