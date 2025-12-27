"""
Writing of results to a command line or file.

Copyright 2026. Andrew Wang.
"""
from typing import Dict, Optional
from pprint import pprint
from json import dump


def print_results(men_engage: Dict[str, Optional[str]],
                  women_engage: Dict[str, Optional[str]],
                  output: Optional[str]):
    """Write smp results to output or command line if None."""
    sorted_male = {k: men_engage[k] for k in sorted(men_engage.keys())}
    sorted_female = {k: women_engage[k] for k in sorted(women_engage.keys())}
    out_json = {'MAN_TO_WOMAN': sorted_male, 'WOMAN_TO_MAN': sorted_female}
    if output is None:
        pprint(out_json)
    else:
        with open(output, 'w', encoding='UTF-8') as fout:
            dump(out_json, fout, indent=2)
