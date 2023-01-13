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

# Using button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just_pressed",
    "button_still_pressed": "still_pressed",
    "button_released": "released",
}

# new pallet for filled text
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
