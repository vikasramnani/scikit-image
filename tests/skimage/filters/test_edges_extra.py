import numpy as np
from numpy.testing import assert_array_equal

from _skimage2.filters.edges import edge_strength_sum as edge_strength_sum_impl
from skimage.filters.edges import edge_strength_sum


def test_edge_strength_sum():
    assert edge_strength_sum is edge_strength_sum_impl
    assert edge_strength_sum(-3, 4) == 7
    assert_array_equal(
        edge_strength_sum(np.array([-1.0, 2.0]), np.array([3.0, -4.0])),
        np.array([4.0, 6.0]),
    )
