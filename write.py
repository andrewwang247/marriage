"""Writing of results to a command line or file."""


def sort_two_dict(dict_1, dict_2):
    """Return two dictionary that are sorted by key."""
    print('Sorting names in alphabetical order...')
    sorted_1 = {k: dict_1[k] for k in sorted(dict_1.keys())}
    sorted_2 = {k: dict_2[k] for k in sorted(dict_2.keys())}
    return sorted_1, sorted_2


def print_results(men_engage, women_engage, output):
    """Write smp results to output or command line if None."""
    male_engage, female_engage = sort_two_dict(men_engage, women_engage)
    if output is None:
        print('\nMAN --> WOMAN')
        for man, his_gf in male_engage.items():
            print('{} --> {}'.format(man, his_gf))
        print('\nWOMAN --> MAN')
        for woman, her_bf in female_engage.items():
            print('{} --> {}'.format(woman, her_bf))
    else:
        print('Writing solution to {}...'.format(output))
        with open(output, 'w') as fout:
            fout.write('MAN --> WOMAN\n')
            for man, his_gf in male_engage.items():
                fout.write('{} --> {}\n'.format(man, his_gf))
            fout.write('\nWOMAN --> MAN\n')
            for woman, her_bf in female_engage.items():
                fout.write('{} --> {}\n'.format(woman, her_bf))
