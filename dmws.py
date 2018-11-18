#! /usr/bin/env python3

"""Script to make a dual monitor wallpaper out of two images.

Takes two images of the same ratio, resizes the larger image to the smaller
one's dimensions, and stitches them horizontally.
"""

import sys
from PIL import Image


def stitch(left_img, right_img, full_img):
    """Stitches two images of the same size horizontally.

    Takes the paths of a left and a right image of the same dimensions,
    stitches them, and stores the resulting image in the path pointed to
    by `full_img'.
    """

    left = Image.open(left_img)
    right = Image.open(right_img)


    full = Image.new('RGB', (left.size[0]*2, left.size[1]))
    full.paste(left, (0, 0, *left.size))
    full.paste(right, (left.size[0], 0, *full.size))
    full.save(full_img)


if __name__ == '__main__':
    stitch(*sys.argv[1:4])
