#!/usr/bin/env python3
# Created By: Kent G
# Date: Jan. 17th, 2023
# This Program is a gamed called space aliens invasion
# where the player fights off an invasion of space aliens.
# Modules used.

import ugame
import stage


def game_scene():

    # Gets images from file (16x16) and sets it as the stage.
    # Background
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Sprite
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(image_bank_background, 10, 8)
    # Initializes the ship variable to a sprite from image bank sprites and gets the fifth image and sets x = 75 y= 66
    ship = stage.Sprite(image_bank_sprites, 4, 75, 66)
    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, 60)
    # Creates a list of layers for the game (In order left appear first)
    game.layers = [ship] + [background]
    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()
    # Place Holder
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("SELECT")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)

        # Update game logic.
        # Redraw sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
