#!/usr/bin/env python3
from ev3dev2.display import Display
from math import sin, cos
import time

display = Display()
display.clear()
display.line(False, 10, 10, 50, 50, 'black', 1)
display.update()

# Can be set to anyhing you like. offset 100:60 seems to be the center of the screen.
rotation = (80, 0)
size = 20
offset = (100, 60)

def get_2d_from_3d(position: tuple):
    # position format = (x, y, z)
    i_3dx = cos(rotation[1]) * position[0] - sin(rotation[1]) * position[1]
    i_3dy = cos(rotation[0]) * (sin(rotation[1]) * position[0] + cos(rotation[1]) * position[1]) - sin(rotation[0]) * position[2]
    i_3dz = sin(rotation[0]) * (sin(rotation[1]) * position[0] + cos(rotation[1]) * position[1]) + cos(rotation[0]) * position[2]
    tS = (i_3dz + 10) * (size / 10)
    result_x = i_3dx * tS + offset[0]
    result_y = i_3dy * tS + offset[1]
    return (result_x, result_y)

def draw_line(start: tuple, end: tuple):
    # start/end format = (x, y, z)
    a = get_2d_from_3d(start)
    b = get_2d_from_3d(end)
    display.line(False, a[0], a[1], b[0], b[1], 'black', 2)

def draw_square(x1: int, x2: int, z1: int, z2: int, y: int):
    # Square only needs one y value since it's 2D
    draw_line((x1, y, z1), (x1, y, z2))
    draw_line((x1, y, z2), (x2, y, z2))
    draw_line((x2, y, z2), (x2, y, z1))
    draw_line((x1, y, z1), (x2, y, z1))

def draw_cube():
    # These are the vertices of the list
    draw_square(1, -1, 1, -1, -1)
    draw_square(1, -1, 1, -1, 1)
    draw_line((1, 1, 1), (1, -1, 1))
    draw_line((1, 1, -1), (1, -1, -1))
    draw_line((-1, 1, 1), (-1, -1, 1))
    draw_line((-1, 1, -1), (-1, -1, -1))

print('starting')
while True:    
    display.clear()
    draw_cube()
    display.update()
    x_rot = rotation[0] + 1
    y_rot = rotation[1] + 2
    rotation = (x_rot, y_rot)
    time.sleep(0.1) # I have not figured out how to make this smooth