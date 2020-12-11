# GEOG0096 - 2nd Assignment (Group Programming Project)
# Task 1 & 2 - Drafts
# Student Name: Hongmin Du
# Student Number: 20066724

# The ideas of making those codes mainly referred to the lecture slides and Jupyter Notebook notes.
# Official tutorials of used python packages were also referred.
# This software should be run with the given materials, some packages for GIS will need to be imported before running this project.


# 0.1 - Import required packages for the following steps
import math
from linecache import getline
import numpy as np
ELEVATION_RADIUS = 5000

# 0.2 - Title for the software and its background:
print("**** GEOG0096 Assignement 2 - Flood Emergency Planning - Dragonfly (0.1) ****")
print()
print("Extreme flooding is expected on the Isle of Wightand, and the authority in charge of planning the emergency response is advising everyone to proceed by foot to the nearest high ground.")
print("This software will give the quickest route from the user's current location to the highest point within a 5km radius in the chosen area.")
print()


# Task 1. User Input
# In this task, this software should:
# Ask the user to input their current location as a British National Grid coordinate (easting and northing)
# Test whether the user is within a box (430000, 80000) and (465000, 95000)

# 1.0 - Introduction
print("Firstly, let's check whether your location is included in the testing area!")

# 1.1 - Define: Point
# The user should input the number of both easting and northing to make a point for the location in the following checks.
class Point:
    def __init__(self, easting, northing):
        self.easting = easting
        self.northing = northing
        if 430000 <= easting <= 465000 and 80000 <= northing <= 95000:
            print("This location can be tested by this software!")
        else:
            print("This location is outside the testing area! Please enter another location!")

# 1.2 - Let the user input the easting and northing and test whether the point is in the testing area
# Notice: the easting and northing should follow the style of British National Grid
easting = int(input('Please input the value of easting: '))
northing = int(input('Please input the value of northing: '))
p = Point(easting, northing)


# Task 2. Highest Point Identification
# In this task, this software should:
# Identify the highest point within a 5km radius from the user location.

# 2.0 - Introduction
print("Secondly, let's find the highest point within a 5km radius from the user location!")

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
