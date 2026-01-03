"""
Utilities to read and validate input for matching.

Copyright 2026. Andrew Wang.
"""
from json import load
from typing import Dict, List, Set, Tuple


def _import_smp(filename: str) -> Tuple[Dict[str, List[str]],
                                        Dict[str, List[str]]]:
    """Read and format contents of filename for smp."""
    # Open file and return men and women preferences separately.
    with open(filename, encoding='UTF-8') as fin:
        preferences = load(fin)
    men_pref: Dict[str, List[str]] = preferences['men']
    women_pref: Dict[str, List[str]] = preferences['women']
    # Do rudimentary length checks.
    assert len(men_pref) > 0, 'Missing data for men'
    assert len(women_pref) > 0, 'Missing data for women'
    assert len(men_pref) == len(
        women_pref), 'Requires equal number of men and women'
    print(f'Detected {len(men_pref)} individuals of each gender.')
    return men_pref, women_pref


def _validate_input(men_pref: Dict[str, List[str]],
                    women_pref: Dict[str, List[str]]):
    """Ensure that the input for smp is valid."""
    print('Validating json input...')

    # Check each man's preferences is a permutation of the women.
    women: Set[str] = set(women_pref.keys())
    for man, mans_pref in men_pref.items():
        unordered_man_pref: Set[str] = set(mans_pref)
        assert len(unordered_man_pref) == len(mans_pref), \
            f'Man {man} has duplicate in preference list.'
        assert unordered_man_pref == women, \
            f'Man {man}\'s preferences do not match women.'

    # Check each woman's preferences is a permutation of the men.
    men: Set[str] = set(men_pref.keys())
    for woman, womans_pref in women_pref.items():
        unordered_woman_pref: Set[str] = set(womans_pref)
        assert len(unordered_woman_pref) == len(womans_pref), \
            f'Woman {woman} has duplicate in preference list.'
        assert unordered_woman_pref == men, \
            f'Woman {woman}\'s preferences do not match men.'


def get_smp(filename: str) -> Tuple[Dict[str, List[str]],
                                    Dict[str, List[str]]]:
    """Read then validate smp input from filename."""
    men_pref, women_pref = _import_smp(filename)
    _validate_input(men_pref, women_pref)
    return men_pref, women_pref
