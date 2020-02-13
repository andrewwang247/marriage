"""Stable Marriage Problem solution using Gale-Shapley."""
import click
from read_validate import get_smp
from marriage import compute_smp
from write import print_results


@click.command()
@click.option('--input', '-i', required=True,
              type=click.Path(exists=True, file_okay=True, dir_okay=False),
              help='Path to input file on which to run SMP algorithm.')
@click.option('--output', '-o', required=False,
              type=click.Path(exists=False, file_okay=True, dir_okay=False),
              help='Path to output file in which to print results.')
def main(input, output):
    """Execute smp algorithm on input and print results to output."""
    men_pref, women_pref = get_smp(input)
    men_engage, women_engage = compute_smp(men_pref, women_pref)
    print_results(men_engage, women_engage, output)


if __name__ == '__main__':
    main()
