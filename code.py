#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Jan 9th
# This program is the "Space Aliens" program on the pyBadge.

import ugame
import stage
 

def game_scene():
    # This function is the main game_scene

    # Imagine banks for CircuitPython
    image_bank_background = stage.bank.from_bmp16("space_aliens_background.bmp")

    # set the background to image 0 in the image bank
    #    and the size (10x8 tiles of size 16x16)
    background = stage.grid(image_bank_background, 10, 8)

    # create a stage for the background to show up on
    #   and set the grame to 60fps
    game = stage.stage(ugame.display, 60)
    #set the layers of all sprites, items show up in order
    game.layers = [background]
    # render all sprites
    #   most likely you will only render the background once per game scene
    game.render_block()
    # repeat forever, game loop
    while True:
        pass


if __name__ == "__main__":
    game_scene()
