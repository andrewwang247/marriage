"""
Utilities to read and validate input for matching.

Copyright 2020. Siwei Wang.
"""
from os import path
from json import load
from typing import Dict, List, Set, Tuple


def read_smp(filename: str) -> Tuple[Dict[str, List[str]],
                                     Dict[str, List[str]]]:
    """Read and format contents of filename for smp."""
    # Make sure that the file is json.
    if path.splitext(filename)[1] != '.json':
        raise ValueError('Input data must be in json file.')
    # Open file and return men and women preferences separately.
    with open(filename, encoding='UTF-8') as fin:
        preferences = load(fin)
    men_pref: Dict[str, List[str]] = preferences['men']
    women_pref: Dict[str, List[str]] = preferences['women']
    # Do rudimentary length checks.
    if len(men_pref) == 0 or len(women_pref) == 0:
        raise ValueError('Input json is missing data for one of the genders.')
    if len(men_pref) != len(women_pref):
        raise ValueError('There must be equal numbers of men and women.')
    print(f'Detected {len(men_pref)} individuals of each gender.')
    return men_pref, women_pref


def validate_smp_input(men_pref: Dict[str, List[str]],
                       women_pref: Dict[str, List[str]]):
    """Ensure that the input for smp is valid."""
    print('Validating json input...')

    # Check each man's preferences is a permutation of the women.
    women: Set[str] = set(women_pref.keys())
    for man, mans_pref in men_pref.items():
        unordered_man_pref: Set[str] = set(mans_pref)
        if len(unordered_man_pref) != len(mans_pref):
            raise ValueError(f'Man {man} has duplicate in preference list.')
        if unordered_man_pref != women:
            raise ValueError(f'Man {man}\'s preferences do not match women.')

    # Check each woman's preferences is a permutation of the men.
    men: Set[str] = set(men_pref.keys())
    for woman, womans_pref in women_pref.items():
        unordered_woman_pref: Set[str] = set(womans_pref)
        if len(unordered_woman_pref) != len(womans_pref):
            raise ValueError(
                f'Woman {woman} has duplicate in preference list.')
        if unordered_woman_pref != men:
            raise ValueError(
                f'Woman {woman}\'s preferences do not match women.')


def get_smp(filename: str) -> Tuple[Dict[str, List[str]],
                                    Dict[str, List[str]]]:
    """Read then validate smp input from filename."""
    men_pref, women_pref = read_smp(filename)
    validate_smp_input(men_pref, women_pref)
    return men_pref, women_pref
