# DEMO deliberate layout violation
import numpy as np
from skimage.filters import sobel


def test_sobel_keeps_shape():
    image = np.zeros((5, 5))
    assert sobel(image).shape == (5, 5)
