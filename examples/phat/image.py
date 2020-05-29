#!/usr/bin/env python

import os
import argparse
from PIL import Image
from inky import InkyPHAT


print("""Inky pHAT: Image test""")

# Get the current path

PATH = os.path.dirname(__file__)

# Command line arguments to set display type and colour

parser = argparse.ArgumentParser()
parser.add_argument('--colour', '-c', type=str, default="red", choices=["red", "black", "yellow"], help="ePaper display colour")
parser.add_argument('--lut', '-l', type=str, default=None, help="override ePaper drawing LUT")
parser.add_argument('--image', '-i', type=str, default="resources/aruco_mip_36h12_00000_212x104.png", help="Image path")
args = parser.parse_args()
colour = args.colour
lut = args.lut
image = args.image

# Set up the display
inky_display = InkyPHAT(colour, lut)

# Set the image to show, and reduce colour palette to black/white or black/white/red
palette = Image.new('P', (1, 1))
if colour == 'black':
    colours = 2
    palette.putpalette(
    [
        255, 255, 255,   # 0 = White
        0, 0, 0,         # 1 = Black
    ] + [0, 0, 0] * 254  # Zero fill the rest of the 256 colour palette
    )
else:
    colours = 3
    palette.putpalette(
    [
        255, 255, 255,   # 0 = White
        0, 0, 0,         # 1 = Black
        255, 0, 0,       # 2 = Red/Yellow
    ] + [0, 0, 0] * 253  # Zero fill the rest of the 256 colour palette
    )

img = Image.open(image)
img = img.quantize(colors=colours, palette=palette)

# Display the image
inky_display.set_image(img)
inky_display.show()
