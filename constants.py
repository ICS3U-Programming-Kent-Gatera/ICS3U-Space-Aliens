#!/usr/bin/env python3
# Created By: Kent G
# Date: Jan. 17th, 2023
# Constants for the CPT's code


SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
SPRITE_MOVEMENT_SPEED = 1
FPS = 60
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS = 5
SHIP_SPEED = 1
ALIEN_SPEED = 1
LASER_SPEED = 2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE

# Using button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just_pressed",
    "button_still_pressed": "still_pressed",
    "button_released": "released",
}

# new palette for filled text
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
