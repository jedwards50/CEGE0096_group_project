# GEOG0096 - 2nd Assignment (Group Programming Project)
# Task 1 & 2 - Drafts
# Student Name: Hongmin Du
# Student Number: 20066724

# The ideas of making those codes mainly referred to the lecture slides and Jupyter Notebook notes.
# Official tutorials of used python packages were also referred.
# This software should be run with the given materials, some packages for GIS will need to be imported before running this project.


# 0. Import required packages for the following steps
import math
from linecache import getline
import numpy as np

ELEVATION_RADIUS = 5000


# Task 1. User Input

# In this task, this software should:
# Ask the user to input their current location as a British National Grid coordinate (easting and northing)
# Test whether the user is within a box (430000, 80000) and (465000, 95000)

# 1.1 Introduction: 
print("Extreme flooding is expected on the Isle of Wightand, the authority in charge of planning the emergency response is advising everyone to proceed by foot to the nearest high ground.")
print("This software will give the quickest route from the user's current location to the highest point within a 5km radius in the chosen area .")
print("Firstly, let's check whether your location is included in the testing area!")

# 1.2 Let the user input the easting of British National Grid and test
coord=input("Please input easting of British National Grid:\n")
easting = int(coord)
if 430000 <= easting <= 465000:
    pass
    print("This easting is included in the testing area!")
else:
    print("Easting not in 430000 465000, please inter another easting!")
    exit(0)

# 1.3 Let the user input the northing of British National Grid and test
coord=input("Please input northing of British National Grid:\n")
northing = int(coord)
if 80000 <= northing <= 95000:
    pass
    print("This northing is included in the testing area!")
else:
    print("Northing not in 80000 95000, please inter another northing!")
    exit(0)
    
# 1.4 Print the point of user's location
p = (easting, northing)
print("According to the British National Grid, the user's location is:")
print(p)
print("This inputted location is included in the testing area, and could be test in the following steps!")


# Task 2. Highest Point Identification

# In this task, this software should:
# Identify the highest point within a 5km radius from the user location.

# 2.1 Limit the size of the elevation array
source = r'.\Material\elevation\SZ.asc'
asc_header = [getline(source, i) for i in range(1, 6)]
header_values = [int(h.split(" ")[-1].strip()) for h in asc_header]
cols, rows, lx, ly, cell = header_values
# print("header_values")
# print(header_values)
asc_index_x = math.floor((easting - lx) // cell)
asc_index_y = math.floor((northing - ly) // cell)
# print("asc_index_x", "asc_index_y")
# print(asc_index_x, asc_index_y)
rows_to_skip = 5 + asc_index_x - (ELEVATION_RADIUS // cell)
max_rows = (ELEVATION_RADIUS // cell) * 2 + 1
start_col = asc_index_x - 1000
end_col = asc_index_x + 1000 + 1
# print(start_col, end_col)
# print(max_rows, rows_to_skip)

# 2.2 Create the 5km buffer to clip the elevation array
elev_arr = np.loadtxt(r'.\Material\elevation\SZ.asc', skiprows=rows_to_skip, max_rows=max_rows, usecols=range(start_col,end_col))
# print(elev_arr.max())
# print(elev_arr.shape)
highest_elevation = np.unravel_index(elev_arr.argmax(), elev_arr.shape)
# print(highest_elevation)
h_x_index = highest_elevation[1] - (ELEVATION_RADIUS // cell) * 2
h_y_index = highest_elevation[0] - (ELEVATION_RADIUS // cell) * 2
bng_easting = (h_x_index + asc_index_x) * cell + lx
bng_northing = (h_y_index + asc_index_y) * cell + ly
print((bng_easting, bng_northing))
