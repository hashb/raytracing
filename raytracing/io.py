"""File io primitives
"""

import cv2


def export(filename, data):
    """
    """
    return cv2.imwrite(filename, data)
