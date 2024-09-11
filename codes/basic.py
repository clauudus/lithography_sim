# -*- coding: utf-8 -*-
"""
First version simulation of a printing of on a wafer.
Semicons and photonics
Clàudia Pàmies, UAB

First version started on the 10th of September 2024.

The objective of this first version of the code is to print a very simple
geometric pattern, chosen by the user, in a determinated user-choosen area.
After this, it should be printed to see the result.

After completing this part of the project, the idea is to implement 
more complex patterns to print on the simulated wafer designed with the 
CAD tool.

At some point, we will have a graphic interface to ensue a user-friendly
simulation where the user will be able to see it's own desingn printed on
a wafer with it's desired size.
"""

import numpy as np
import matplotlib.pyplot as plt

wafer_size = 100
wafer = np.zeros((wafer_size, wafer_size))

# Ask the user to choose a geometric pattern
pattern_type = input("Choose a pattern (circle, square, triangle): ").lower()

def print_circle(wafer, center=(50, 50), radius=10):
    for i in range(wafer_size):
        for j in range(wafer_size):
            if np.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2) <= radius:
                wafer[i, j] = 1
    return wafer

def print_square(wafer, center=(50, 50), side_length=10):
    half_side = side_length // 2
    for i in range(max(0, center[0] - half_side), min(wafer_size, center[0] + half_side)):
        for j in range(max(0, center[1] - half_side), min(wafer_size, center[1] + half_side)):
            wafer[i, j] = 1
    return wafer

def print_triangle(wafer, center=(50, 50), height=10):
    for i in range(center[0], center[0] + height):
        for j in range(center[1] - (i - center[0]), center[1] + (i - center[0]) + 1):
            if 0 <= i < wafer_size and 0 <= j < wafer_size:
                wafer[i, j] = 1
    return wafer

#Let the user choose the size for the geometric form to print
if pattern_type == "circle":
    radius = int(input("Introduce the desired radius for the circular pattern: "))
    parameters = {'radius': radius}
elif pattern_type == "square":
    side_length = int(input("Introduce the desired side length for the square pattern: "))
    parameters = {'side_length': side_length}
elif pattern_type == "triangle":
    height = int(input("Introduce the desired height for the triangular pattern: "))
    parameters = {'height': height}
else:
    print("Error, unknown pattern type.")
    exit()

#Making sure the user-choosen size is in the limits of the wafer
max_size = wafer_size // 2

if (pattern_type == "circle" and parameters['radius'] > max_size) or \
   (pattern_type == "square" and parameters['side_length'] > wafer_size) or \
   (pattern_type == "triangle" and parameters['height'] > wafer_size):
    print("Error, size too big for the wafer.")
    exit()

patterns = {
    "circle": lambda wafer: print_circle(wafer, radius=parameters['radius']),
    "square": lambda wafer: print_square(wafer, side_length=parameters['side_length']),
    "triangle": lambda wafer: print_triangle(wafer, height=parameters['height'])
}

if pattern_type in patterns:
    wafer_with_pattern = patterns[pattern_type](wafer)
    plt.imshow(wafer_with_pattern, cmap='gray')
    plt.title(f'Lithography pattern simulation on Wafer (Pattern={pattern_type.capitalize()})')
    plt.show()
else:
    print("Error, unknown pattern type.")
