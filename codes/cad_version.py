# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:52:20 2024

@author: claud

Second version simulation of a printing of on a wafer.
Semicons and photonics
Clàudia Pàmies, UAB

In this second version I'll try to implement a way to import CAD-made documents so the 
user can print their own pattern on the simulated wafer.

I'll be using the ezdxf library to read the .dxf file. I am still using a 100x100 grid to
print the patterns. I'll try to make it more dynamic so the user can choose between a
range of values for the grid but right now I'll keep working with this to make it easier
for me while I am still working on the code.

I'll try to change it for the graphic/interactive interface I would like to do.

I am currently makeing the user choose by writing the name of the file to import it.
I'll change it for the next version.

Note: To use the ezdxf library you should install it by using the command:

pip install ezdxf

That's all for today :)
"""

import numpy as np
import matplotlib.pyplot as plt
import ezdxf

wafer_size = 100
wafer = np.zeros((wafer_size, wafer_size))

def dxf_to_wafer_grid(dxf_file, wafer_size):
    wafer_grid = np.zeros((wafer_size, wafer_size))
    
    #Load file
    doc = ezdxf.readfile(dxf_file)
    msp = doc.modelspace()

    # Iterate over all entities in the model space
    for entity in msp:
        if entity.dxftype() == 'CIRCLE':
            center = entity.dxf.center
            radius = entity.dxf.radius

            # Convert the circle to grid coordinates
            center_x = int(center[0] * wafer_size / 100)
            center_y = int(center[1] * wafer_size / 100)
            radius_grid = int(radius * wafer_size / 100)

            #Draw the circle
            for i in range(wafer_size):
                for j in range(wafer_size):
                    if np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2) <= radius_grid:
                        wafer_grid[i, j] = 1

        #I should add other entities (e.g., LINES, POLYLINE) similarly

    return wafer_grid

# Load the CAD file and convert it to the wafer grid
dxf_file = "your_pattern.dxf"  # Replace with the DXF file name
wafer_with_pattern = dxf_to_wafer_grid(dxf_file, wafer_size)

# Visualize the pattern on the wafer
plt.imshow(wafer_with_pattern, cmap='gray')
plt.title('Lithography pattern simulation on Wafer (from CAD)')
plt.show()
