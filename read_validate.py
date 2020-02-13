"""Utilities to read and validate input for matching."""
from os import path
from json import load


def read_smp(filename):
    """Read and format contents of filename for smp."""
    # Make sure that the file is json.
    if path.splitext(filename)[1] != '.json':
        raise ValueError('Input data must be in json file.')
    # Open file and return men and women preferences separately.
    with open(filename, 'r') as fin:
        preferences = load(fin)
        return preferences['men'], preferences['women']


def validate_smp_input(men_pref, women_pref):
    """Ensure that the input for smp is valid."""
    print('Validating json input...')
    # Do rudimentary length checks.
    if len(men_pref) == 0 or len(women_pref) == 0:
        raise ValueError('Input json is missing data for one of the genders.')
    if len(men_pref) != len(women_pref):
        raise ValueError('There must be equal numbers of men and women.')

    # Check each man's preferences is a permutation of the women.
    women = set(women_pref.keys())
    for man, mans_pref in men_pref.items():
        unordered_pref = set(mans_pref)
        if len(unordered_pref) != len(mans_pref):
            raise ValueError(
                'Man {} has duplicate in preference list.'.format(man))
        if unordered_pref != women:
            raise ValueError(
                'Man {}\'s preferences do not match women.'.format(man))

    # Check each woman's preferences is a permutation of the men.
    men = set(men_pref.keys())
    for woman, womans_pref in women_pref.items():
        unordered_pref = set(womans_pref)
        if len(unordered_pref) != len(womans_pref):
            raise ValueError(
                'Woman {} has duplicate in preference list.'.format(woman))
        if unordered_pref != men:
            raise ValueError(
                'Woman {}\'s preferences do not match women.'.format(woman))


def get_smp(filename):
    """Read then validate smp input from filename."""
    men_pref, women_pref = read_smp(filename)
    validate_smp_input(men_pref, women_pref)
    return men_pref, women_pref
