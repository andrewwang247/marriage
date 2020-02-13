"""Automated test generator for Stable Marriage problem."""
import json
from random import shuffle
from copy import deepcopy


def get_names():
    """Shuffle names in files."""
    with open('Test/male-names.txt', 'r') as fin:
        male_names = [line.rstrip() for line in fin]
    with open('Test/female-names.txt', 'r') as fin:
        female_names = [line.rstrip() for line in fin]
    shuffle(male_names)
    shuffle(female_names)
    return male_names, female_names


def construct_pref(men, women):
    """Construct preferences from two lists."""
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
    males, females = get_names()
    assert len(males) == len(females)

    preferences = construct_pref(males, females)
    with open('Test/large_smp.json', 'w') as fin:
        json.dump(preferences, fin, indent=4)


if __name__ == '__main__':
    main()
