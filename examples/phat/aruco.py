#!/usr/bin/env python

import os
import argparse
from PIL import Image
from inky import InkyWHAT, InkyPHAT


print("""Inky pHAT: ArUco tag test

aruco_mip_36h12_00000

""")

# Get the current path

PATH = os.path.dirname(__file__)

# Set up the correct display and scaling factors

inky_display = InkyPHAT("black")
# inky_display.set_border(inky_display.BLACK)

# Set the image to show, and reduce colour palette to black and white

palette = Image.new('P', (1, 1))
palette.putpalette(
[
    255, 255, 255,   # 0 = White
    0, 0, 0,         # 1 = Black
] + [0, 0, 0] * 254  # Zero fill the rest of the 256 colour palette
)

img = Image.open(os.path.join(PATH, "resources/aruco_mip_36h12_00000_212x104.png"))
img = img.quantize(colors=2, palette=palette)

# Display the tag image
inky_display.set_image(img)
inky_display.show()
