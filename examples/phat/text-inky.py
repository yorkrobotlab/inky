#!/usr/bin/env python3
from inky import InkyPHAT
from PIL import Image, ImageDraw, ImageFont
import argparse

parser = argparse.ArgumentParser(description="Draw text on e-ink.")
parser.add_argument("line1", type=str, help="text line 1")
parser.add_argument("line2", type=str, nargs='?', default=None, help="text line 2")
parser.add_argument("-f", "--font", type=str, default="DejaVuSans-Bold.ttf", help="main font")
parser.add_argument("-s", "--size", type=int, default=36, help="main font size")
parser.add_argument("-c", "--colour", type=int, default=1, help="main colour")
parser.add_argument("--font2", type=str, default=None, help="different second line font")
parser.add_argument("--size2", type=int, default=None, help="different second line size")
parser.add_argument("--colour2", type=int, default=None, help="different second line colour")
args = parser.parse_args()

font1 = args.font
size1 = args.size
colour1 = args.colour

font2 = args.font2 if args.font2 is not None else font1
size2 = args.size2 if args.size2 is not None else size1
colour2 = args.colour2 if args.colour2 is not None else colour1

line1 = args.line1
line2 = args.line2

palette = [
	255, 255, 255,   # 0 = White
	0, 0, 0,         # 1 = Black
	255, 0, 0,       # 2 = Red
] + [0, 0, 0] * 253  # Zero fill the rest of the 256 colour palette

screen = Image.new("P", (212, 104), 0)
screen.putpalette(palette)

font1 = ImageFont.truetype(font1, size1)
font2 = ImageFont.truetype(font2, size2)

draw = ImageDraw.Draw(screen)

text_width, text_height = font1.getsize(line1)

if line2 is None:
	draw.text((212 / 2 - text_width / 2, 104 / 2 - text_height / 2), line1, colour1, font=font1)
else:
	text2_width, text2_height = font2.getsize(line2)
	draw.text((212 / 2 - text_width / 2, 104 / 4 - text_height / 2), line1, colour1, font=font1)
	draw.text((212 / 2 - text2_width / 2, (104 * 3) / 4 - text2_height / 2), line2, colour2, font=font2)

inky_display = InkyPHAT("red")
inky_display.set_image(screen)
inky_display.show()
