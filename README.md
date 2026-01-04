# Matching

Solver for the [stable matching problem](https://en.wikipedia.org/wiki/Stable_marriage_problem) using the Gale-Shapley algorithm.

## Usage

```text
Usage: main.py [OPTIONS]

  Execute smp algorithm on input and print results to output.

Options:
  -f, --filename FILE  Path to input json on which to run SMP algorithm.
                       [required]
  --help               Show this message and exit.
```

The output to stdout is in JSON format and can be redirected into a file if desired.

## Format

The input must be a JSON object structured as follows:

```json
{
  "men": {
    "man_1": [
      "woman_1",
      "woman_2",
      "woman_3"
    ],
    "man_2": [
      "woman_3",
      "woman_2",
      "woman_1"
    ],
    "man_3": [
      "woman_1",
      "woman_3",
      "woman_2"
    ]
  },
  "women": {
    "woman_1": [
      "man_2",
      "man_1",
      "man_3"
    ],
    "woman_2": [
      "man_3",
      "man_2",
      "man_1"
    ],
    "woman_3": [
      "man_3",
      "man_1",
      "man_2"
    ]
  }
}
```

where each list is in decreasing order of that individual's preference. See `test/small_smp.json` for a real example.

## Algorithms

The [Gale-Shapley algorithm](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm) runs in $O(n^2)$ time for two groups of $n$ individuals. After execution, the program checks its solution to ensure correctness.

## Files

The program is split into logical chunks.

- `main.py` is the highest level layer that interfaces with the user and delegates computations.
- `read_validate.py` reads json input and ensures that input is valid.
- `matching.py` contains the core of the Gale-Shapley algorithm.

## Testing

All static testing material is contained in the `tst` directory. The script `generator.py` (run without arguments) uses `tst/female-names.txt` and `tst/male-names.txt` to generate valid json input for SMP, which it places in `tst/large_smp.json`. Note that `tst/small_smp.json` is also available as a more human-friendly test case. Run `pytest` to validate solutions for all `tst/*_smp.json` files.
