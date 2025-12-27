"""
Automated test generator for Stable Marriage problem.

Copyright 2026. Andrew Wang.
"""
from json import dump
from random import shuffle
from copy import deepcopy
from typing import List, Dict


def read_names(name_file: str) -> List[str]:
    """Read names listed in name file."""
    with open(name_file, encoding='UTF-8') as fin:
        names: List[str] = [line.rstrip() for line in fin]
    assert len(names) == len(set(names))
    return names


def construct_pref(men: List[str], women: List[str]) \
        -> Dict[str, Dict[str, List[str]]]:
    """Construct preferences from two lists."""
    print('Constructing preferences...')
    male_pref = {}
    for man in men:
        my_pref = deepcopy(women)
        shuffle(my_pref)
        male_pref[man] = my_pref

    female_pref = {}
    for woman in women:
        my_pref = deepcopy(men)
        shuffle(my_pref)
        female_pref[woman] = my_pref

    return {
        'men': male_pref,
        'women': female_pref
    }


def main():
    """Generate an automated test case."""
    print('Reading and shuffling names...')
    males = read_names('tst/male-names.txt')
    females = read_names('tst/female-names.txt')
    assert len(males) == len(females)

    preferences = construct_pref(males, females)
    print('Writing json to file...')
    with open('tst/large_smp.json', 'w', encoding='UTF-8') as fin:
        dump(preferences, fin, indent=2)


if __name__ == '__main__':
    main()
