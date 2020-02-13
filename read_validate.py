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


def read_srp(filename):
    """Read and format contets of filename for srp."""
    # Make sure that the file is json.
    if path.splitext(filename)[1] != '.json':
        raise ValueError('Input data must be in json file.')
    with open(filename, 'r') as fin:
        return load(fin)


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


def validate_srp_input(rm_pref):
    """Ensure that the input for srp is valid."""
    print('Validating json input...')
    if len(rm_pref) == 0:
        raise ValueError('Input json is missing roommate data.')

    # Check each roommate's preference is a permutation of the roomates.
    roommates = set(rm_pref.keys())
    for mate, pref in rm_pref.items():
        unordered_pref = set(pref)
        if len(unordered_pref) != len(pref):
            raise ValueError(
                '{} has duplicate in preference list.'.format(mate))
        roommates.remove(mate)
        if unordered_pref != roommates:
            raise ValueError(
                '{}\'s preferences do not match roommates.'.format(mate))
        roommates.add(mate)


def get_smp(filename):
    """Read then validate smp input from filename."""
    men_pref, women_pref = read_smp(filename)
    validate_smp_input(men_pref, women_pref)
    return men_pref, women_pref

def get_srp(filename):
    """Read then validate srp input from filename."""
    rm_pref = read_srp(filename)
    validate_srp_input(rm_pref)
    return rm_pref
