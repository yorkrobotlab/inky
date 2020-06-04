#!/usr/bin/env python3
"""Script to demonstrate Inky differential updates."""
from inky import InkyPHAT
from PIL import Image, ImageDraw


def add_battery_bar(draw, number, colour, filled):
    x = (20 * number) + 6
    if filled:
        fill = colour
    else:
        fill = 0
    draw.rectangle((x, 8, x + 15, 95), fill, colour, 1)


def draw_bars(draw, fill_level):
    for i in range(0, 2):
        filled = fill_level > i
        add_battery_bar(draw, i, 1, filled)
    for i in range(2, 10):
        filled = fill_level > i
        add_battery_bar(draw, i, 1, filled)


def main():
    palette = [
                  255, 255, 255,  # 0 = White
                  0, 0, 0,  # 1 = Black
                  255, 0, 0,  # 2 = Red
              ] + [0, 0, 0] * 253  # Zero fill the rest of the 256 colour palette

    inky_display = InkyPHAT("red")

    screen = Image.new("P", (212, 104), 0)
    screen.putpalette(palette)
    draw = ImageDraw.Draw(screen)
    draw.rectangle((0, 2, 207, 101), 0, 2, 2)
    draw.rectangle((208, 32, 211, 71), 2, 2, 0)
    draw_bars(draw, 10)

    inky_display.set_image(screen)
    inky_display.show(busy_wait=False)

    for i in range(1, 11):
        draw_bars(draw, 10 - i)
        inky_display.set_image(screen)
        inky_display.show_delta()

    for i in range(1, 11):
        draw_bars(draw, i)
        inky_display.set_image(screen)
        inky_display.show_delta()

    inky_display.deep_sleep()


if __name__ == "__main__":
    main()
