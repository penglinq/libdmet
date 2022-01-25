"""
Test
"""

import numpy as np
import libdmet
import pytest

def test_calculate_distance():

    r1 = np.array([0,0,0])
    r2 = np.array([0,0,1])
    
    expected_distance = 1.0

    calculated_distance = libdmet.calculate_distance(r1, r2)

    assert expected_distance - calculated_distance < 1e-7
    #raise RuntimeError

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60  ),
    (np.array([np.sqrt(3)/2, (1/2), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30),
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = libdmet.calculate_angle(p1, p2, p3, degrees=True)

    assert expected_angle == pytest.approx(calculated_angle), F'{calculated_angle} {expected_angle}'