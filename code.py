#!/usr/bin/env python3
# Created By: Kent G
# Date: Jan. 17th, 2023
# This Program is a gamed called space aliens invasion
# where the player fights off an invasion of space aliens.
# Modules used.

import stage
import ugame
import random
import time
import constants


def menu_scene():
    # This function creates a menu scene.
    # Gets images from file (16x16) and sets it as the stage.
    # Background
    image_bank_mt_background = stage.Bank.from_bmp16
    ("mt_game_studio.bmp")
    # Add text objects
    text = []
    text1 = stage.text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studios.")
    text.append(text1)

    text2 = stage.text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    # get sound
    pew_sound = open("pew.wav", "rb")
    sound = ugame.uaudio
    sound.stop()
    sound.mute(False)

    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_Y, constants.SCREEN_GRID_X
    )

    game = game.stage(ugame.display, constants.FPS)
    # Creates a list of layers for the game (In order left appear first)
    game.layers = text + [background]
    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()
    # Place Holder
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene
        game.tick()


def splash_scene():
    # This funtion creates a splash scene.

    # Get sound ready.
    # Playing the coin sound when the game boots up.
    coin_sound = open("coin.wav", "rb")
    sound = ugame.uaudio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # Gets images from file (16x16) and sets it as the stage.
    # Background
    image_bank_mt_background = stage.Bank.from_bmp16
    ("mt_game_studio.bmp")

    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_Y, constants.SCREEN_GRID_X
    )
    # used this program to split the image into tile:

    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    game = game.stage(ugame.display, constants.FPS)
    # Creates a list of layers for the game (In order left appear first)
    game.layers = [background]
    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()
    # Place Holder
    while True:
        # Wait for 2 seconds.
        time.sleep(2)
        menu_scene()


def game_scene():

    # Gets images from file (16x16) and sets it as the stage.
    # Background
    image_bank_background = stage.Bank.from_bmp16
    ("space_aliens_background.bmp")

    # Sprite
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Buttons that you want to keep state information on.
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound
    pew_sound = open("pew.wav", "rb")
    sound = ugame.uaudio
    sound.stop()
    sound.mute(False)

    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_Y, constants.SCREEN_GRID_X
    )
    # Initializes the ship variable to a sprite from image bank sprites and
    # gets the fifth image and sets x = 75 y= 66
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_GRID_X - (2 * constants.SPRITE_SIZE)
    )
    alien = stage.sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )
    # Creating a list for lasers we shoot.
    lasers = []
    for i in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.SPRITE(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        lasers.append(a_single_laser)

    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FPS)
    # Creates a list of layers for the game (In order left appear first)
    game.layers = lasers + [ship] + [alien] + [background]
    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()
    # Place Holder
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        # All these nested if statements check the state of the buttons.
        # They check if the button is pressed, held down or released.
        if keys & ugame.K_X != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("SELECT")
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_DOWN != 0:
            if ship.y <= constants.SCREEN_Y:
                ship.move(ship.x, ship.y + constants.SPRITE_MOVEMENT_SPEED)
            else:
                ship.move(ship.x, 0)
        if keys & ugame.K_UP != 0:
            if ship.y >= 0:
                ship.move(ship.x, ship.y - constants.SPRITE_MOVEMENT_SPEED)
            else:
                ship.move(ship.y, 0)

        # Update game logic.
        # Playing sound if the a button state is "just_pressed."
        if a_button == constants.button_state["button_just_pressed"]:
            for i in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    # play sound
                    sound.play(pew_sound)
                    break
        # each frame move the laser
        for i in range(len(laser)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                if lasers[laser_number].y > constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # Redraw sprites
        game.render_sprites(lasers + [ship] + [alien])
        game.tick()


if __name__ == "__main__":
    splash_scene()
