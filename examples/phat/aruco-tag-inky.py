#!/usr/bin/env python3
import cv2.aruco as aruco
from inky import InkyPHAT
from PIL import Image, ImageDraw, ImageFont
import argparse


def get_tag(tag_id):
	dictionary = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)
	img = aruco.drawMarker(dictionary, tag_id, 104)
	return Image.fromarray(img)


parser = argparse.ArgumentParser(description="Draw DICT_6X6_50 ArUco tag on e-ink.")
parser.add_argument("tag", type=int, nargs='?', default=0, help="tag number to draw")
args = parser.parse_args()

tag_id = args.tag

palette = [
	255, 255, 255,   # 0 = White
	0, 0, 0,         # 1 = Black
	255, 0, 0,       # 2 = Red
] + [0, 0, 0] * 253  # Zero fill the rest of the 256 colour palette

screen = Image.new("P", (212, 104), 0)
screen.putpalette(palette)

font = ImageFont.truetype("DejaVuSans-Bold.ttf", 28)
draw = ImageDraw.Draw(screen)

id_text = "{:02}".format(tag_id)

text_width, text_height = font.getsize(id_text)

text1 = Image.new("P", (text_width, text_height), 0)
text1.putpalette(palette)
draw1 = ImageDraw.Draw(text1)
draw1.text((0, 0), id_text, 2, font=font)
text1 = text1.rotate(270, expand=1)

text2 = Image.new("P", (text_width, text_height), 0)
text2.putpalette(palette)
draw2 = ImageDraw.Draw(text2)
draw2.text((0, 0), id_text, 2, font=font)
text2 = text2.rotate(90, expand=1)

tag = get_tag(tag_id)
tag = tag.remap_palette([1, 0])

screen.paste(text1, (4, 52 - int(text_width / 2)))
screen.paste(text2, (212 - text_height - 4, 52 - int(text_width / 2)))
screen.paste(tag, (54, 0))

inky_display = InkyPHAT("red")
inky_display.set_image(screen)
inky_display.show()
