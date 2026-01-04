"""
Pytest to run unit tests.

Copyright 2026. Andrew Wang.
"""
from glob import glob
from pytest import mark
from read_validate import get_smp
from matching import compute_smp


@mark.parametrize('filename', glob('tst/*_smp.json'))
def test_flow(filename: str):
    """Test network flow on filename."""
    men_pref, women_pref = get_smp(filename)
    compute_smp(men_pref, women_pref)
