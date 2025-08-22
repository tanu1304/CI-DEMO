import pytest
import sys, os

# Ensure project root (parent of tests) is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import calc

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_div():
    assert calc.div(6, 3) == 2
    with pytest.raises(ZeroDivisionError):
        calc.div(1, 0)
