"""
Writing of results to a command line or file.

Copyright 2020. Siwei Wang.
"""
from typing import Dict, Union


def print_results(men_engage: Dict[str, Union[str, None]],
                  women_engage: Dict[str, Union[str, None]],
                  output: Union[str, None]):
    """Write smp results to output or command line if None."""
    print('Sorting names in alphabetical order...')
    sorted_male = {k: men_engage[k] for k in sorted(men_engage.keys())}
    sorted_women = {k: women_engage[k] for k in sorted(women_engage.keys())}
    if output is None:
        print('\nMAN --> WOMAN')
        for man, his_gf in sorted_male.items():
            print(f'\t{man} --> {his_gf}')
        print('\nWOMAN --> MAN')
        for woman, her_bf in sorted_women.items():
            print(f'\t{woman} --> {her_bf}')
    else:
        assert isinstance(output, str)
        print(f'Writing solution to {output}...')
        with open(output, 'w') as fout:
            fout.write('MAN --> WOMAN\n')
            for man, his_gf in sorted_male.items():
                fout.write(f'\t{man} --> {his_gf}\n')
            fout.write('\nWOMAN --> MAN\n')
            for woman, her_bf in sorted_women.items():
                fout.write(f'\t{woman} --> {her_bf}\n')
