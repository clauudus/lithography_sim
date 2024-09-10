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
autoCAD tool.

At some point, we will have a graphic interface to ensue a user-friendly
simulation where the user will be able to see it's own desingn printed on
a wafer with it's desired size.
"""

import numpy as np
import matplotlib.pyplot as plt

wafer_size = 100 #grid with a 100x100 size
wafer = np.zeros((wafer_size, wafer_size))

radius=int(input("introduce the desired radius (for a circular pattern): "))
           
#Here we will define the lithography pattern:
def print_pattern (wafer, pattern_type="circle", center=(50,50), radius=radius):
    for i in range(wafer_size):
        for j in range(wafer_size):
            if pattern_type == "circle":
                if np.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2) <= radius:
                    wafer[i,j] = 1
    return wafer

wafer_with_pattern = print_pattern(wafer, radius=radius)

plt.imshow(wafer_with_pattern, cmap='gray')
plt.title(f'Lithography pattern simulation on Wafer (Radius={radius})')
plt.show()
