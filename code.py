#!/usr/bin/env python3
# Created By: Kent G
# Date: Jan. 17th, 2023
# This Program is a gamed called space aliens invasion
# where the player fights off an invasion of space aliens.
# Modules used.

import ugame
import stage
import constants


def game_scene():

    # Gets images from file (16x16) and sets it as the stage.
    # Background
    image_bank_background = stage.Bank.from_bmp16
    ("space_aliens_background.bmp")
    # Sprite
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_Y, constants.SCREEN_GRID_X
    )
    # Initializes the ship variable to a sprite from image bank sprites and
    # gets the fifth image and sets x = 75 y= 66
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_GRID_X -
        (2 * constants.SPRITE_SIZE)
    )
    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FPS)
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
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_DOWN:
            if ship.y <= constants.SCREEN_Y:
                ship.move(ship.x, ship.y + constants.SPRITE_MOVEMENT_SPEED)
            else:
                ship.move(ship.x, 0)
        if keys & ugame.K_UP:
            if ship.y >= 0:
                ship.move(ship.x, ship.y - constants.SPRITE_MOVEMENT_SPEED)
            else:
                ship.move(ship.y, 0)

        # Update game logic.
        # Redraw sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
