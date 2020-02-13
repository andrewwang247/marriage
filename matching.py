"""
Solutions for the stable marriage and roommates problems.

Uses Gale-Shapley for SMP and Irving for SRP.
"""
from read_validate import get_smp, get_srp
import click


def compute_smp(men_pref, women_pref):
    """
    Compute a stable marriage on two preference lists.

    This function uses the Gale–Shapley algorithm.
    """
    print('Computing stable marriages...')


def compute_srp(rm_pref):
    """
    Compute a stable matching on a single preference list.

    This function uses the Irving algorithm.
    """
    print('Computing stable roommates match...')


@click.command()
@click.option('--algorithm', '-a', required=True, type=str,
              help='Choose SMP or SRP algorithm.')
@click.option('--input', '-i', required=True,
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              help='Path to input file on which to run algorithm.')
@click.option('--output', '-o', required=False,
              type=click.Path(exists=False, file_okay=True, dir_okay=False),
              help='Path to output file in which to print results.')
def main(algorithm, input, output):
    """Execute smp or srp algorithm on input and print results to output."""
    if algorithm == 'smp':
        men_pref, women_pref = get_smp(input)
        compute_smp(men_pref, women_pref)
    elif algorithm == 'srp':
        rm_pref = get_srp(input)
        compute_srp(rm_pref)
    else:
        raise ValueError('Please choose between smp or srp for algorithm.')


if __name__ == '__main__':
    main()
