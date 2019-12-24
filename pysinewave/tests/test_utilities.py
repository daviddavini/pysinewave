import pytest
import math

from pysinewave import utilities

# def test_bounded():
#     # Out-of-bounds values snap to closest bound
#     assert utilities.bounded(6, -2, 3) == 3
#     assert utilities.bounded(-10, -2, 3) == -2
#     # Regardless of order
#     assert utilities.bounded(6, 3, -2) == 3
#     # Inside-bounds values remain unchanged
#     assert utilities.bounded(1, 3, -2) == 1

def test_bounded_by_end():
    # Bounds by end and only end, when end > start
    assert (utilities.bounded_by_end([1,2,3,4,5], 3, 4) == [1,2,3,4,4]).all()
    # Bounds by end and only end, when end < start
    assert (utilities.bounded_by_end([1,2,3,4,5], 3, 2) == [2,2,3,4,5]).all()

def test_pitch_to_frequency():
    # 0 is middle C
    assert utilities.pitch_to_frequency(0) == utilities.MIDDLE_C_FREQUENCY
    # 9 is middle A (440)
    assert math.isclose(utilities.pitch_to_frequency(9), 440, rel_tol=0.1)