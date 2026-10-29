from skimage.filters.edges import edge_strength_sum


def test_edge_strength_sum():
    assert edge_strength_sum(-3, 4) == 7
