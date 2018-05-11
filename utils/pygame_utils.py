import numpy as np


def scale_point(number, scale, screen_center):
    return number * scale + screen_center


scale_points = np.vectorize(scale_point)