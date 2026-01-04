"""
Stable Marriage Problem solution using Gale-Shapley.

Copyright 2026. Andrew Wang.
"""
# pylint: disable=no-value-for-parameter
import logging
from typing import Dict, Optional
from json import dumps
from click import command, option, Path
from read_validate import get_smp
from marriage import compute_smp

logger = logging.getLogger(__name__)


def print_results(men_engage: Dict[str, Optional[str]],
                  women_engage: Dict[str, Optional[str]]):
    """Write smp results to output or command line if None."""
    sorted_male = {k: men_engage[k] for k in sorted(men_engage.keys())}
    sorted_female = {k: women_engage[k] for k in sorted(women_engage.keys())}
    out_json = {'MAN_TO_WOMAN': sorted_male, 'WOMAN_TO_MAN': sorted_female}
    print(dumps(out_json, indent=2))


@command()
@option('--filename', '-f', required=True,
        type=Path(exists=True, file_okay=True, dir_okay=False),
        help='Path to input json on which to run SMP algorithm.')
def main(filename: str):
    """Execute smp algorithm on input and print results to output."""
    men_pref, women_pref = get_smp(filename)
    men_engage, women_engage = compute_smp(men_pref, women_pref, check=False)
    print_results(men_engage, women_engage)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    main()
