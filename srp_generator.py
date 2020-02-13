"""Automated test generator for Stable Roommate problem."""
import json
from random import shuffle
from copy import deepcopy


def get_names():
    """Shuffle names in files."""
    with open('Test/male-names.txt', 'r') as fin:
        male_names = [line.rstrip() for line in fin]
    with open('Test/female-names.txt', 'r') as fin:
        female_names = [line.rstrip() for line in fin]
    names = male_names + female_names
    shuffle(names)
    return names


def construct_pref(names):
    """Construct preferences from one list."""
    pref = {}
    for name in names:
        # Shuffle the rest of the list.
        rm_copy = deepcopy(names)
        rm_copy.remove(name)
        shuffle(rm_copy)
        pref[name] = rm_copy
    return pref


def main():
    """Generate an automated test case."""
    names = get_names()

    preferences = construct_pref(names)
    with open('Test/large_srp.json', 'w') as fin:
        json.dump(preferences, fin, indent=4)


if __name__ == '__main__':
    main()
