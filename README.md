# Matching

Python implementations for the Stable Marriage Problem (SMP) and the Stable Roommates Problem (SRP).

## Usage

Execute with `python3 matching.py` [OPTIONS]

Options:

  -a, --algorithm TEXT:  Choose SMP or SRP algorithm.  [required]

  -i, --input FILE:  Path to input file on which to run algorithm. [required]

  -o, --output FILE:  Path to output file in which to print results.

  --help:  Show this message and exit.

If no output file is provided, the program simply prints to the command line.

## Algorithms

See <https://en.wikipedia.org/wiki/Stable_marriage_problem> for the SMP problem. The Gale-Shapley algorithm for SMP runs in O(n^2) time for two groups of n.

See <https://en.wikipedia.org/wiki/Stable_roommates_problem> for the SRP problem. The Irving algorithm for SRP also runs in O(n^2) time for a single group of n.

After execution, the program checks its solution to ensure correctness.

## Files

The program is split into logical chunks.

- `matching.py` is the highest level layer that interacts delegates computations.
- `read_validate.py` reads json input and ensures that input is valid.
- `marriage.py` contains the Gale-Shapley algorithm.
- `roommate.py` contains the Irving algorithm.
- `write.py` writes solutions to the command line or an output file.

## Testing

All static testing material is contained in the `Test` directory. The scripts `smp_generator.py` and `srp_generator.py` use `Test/female-names.txt` and `Test/male-names.txt` to generate valid json for SMP and SRP respectively.

These randomly generated json files are written to `Test/large_smp.json` and `Test/large_srp.json`. Smaller, more human-friendly test cases are availabe as `Test/small_smp.json` and `Test/small_srp.json`.
