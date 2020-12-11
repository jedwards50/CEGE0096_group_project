# CEGE0096 - 2nd Assignment (Group Programming Project)
# Task 1 & 2 - Drafts

# The ideas of making those codes mainly referred to the lecture slides and Jupyter Notebook notes.
# Official tutorials of used python packages were also referred.
# This software should be run with the given materials, some packages for GIS will need to be imported
# before running this project.


# 0.1 - Import required packages for the following steps
import os
import rasterio
from shapely.geometry import Point
from shapely.geometry import Polygon

elevation_radius = 5000

# 0.2 - Title for the software and its background:
print("**** CEGE0096 Assignment 2 - Flood Emergency Planning - Dragonfly (0.1) ****")
print()
print("Extreme flooding is expected on the Isle of Wight and the authority in charge of planning the "
      "emergency response is advising everyone to proceed by foot to the nearest high ground.")
print("This software will give the quickest route from the user's current location to the highest point "
      "within a 5km radius in the chosen area.")
print()

# Task 1. User Input.
# In this task, this software should:
# Ask the user to input their current location as a British National Grid coordinate (easting and northing).
# Test whether the user is within a box (430000, 80000) and (465000, 95000).

# 1.0 - Introduction
print("Firstly, let's check whether your location is included in the testing area!")

# 1.1 - Let the user input the easting and northing and test whether the point is in the testing area
# Notice: the easting and northing should follow the style of British National Grid
p = Point(float(input('Please input the value of your easting (use British National Grid): ')),
          float(input('Please input the value of your northing (use British National Grid): ')))

testing_area = Polygon([(430000, 80000), (430000, 95000), (465000, 95000), (465000, 80000)])


def check_point_in_box(point, polygon):
    if point.within(polygon):
        print("This location can be tested by this software!")
    else:
        print("This location is outside the testing area! Please enter another location!")


check_point_in_box(p, testing_area)

# Task 2. Highest Point Identification.
# In this task, this software should:
# Identify the highest point within a 5km radius from the user location.

# 2.0 - Introduction.
print("Secondly, let's find the highest point within a 5km radius from the user location!")

# 2.1 - Open elevation file.
# NB: Material folder must be stored in working directory. A .gitignore file can be used to ignore this folder
# when pushing to GitHub. The Material folder cannot be uploaded to GitHub because file sizes are greater than 100MB.
elevation_asc = rasterio.open(os.path.join('Material', 'elevation', 'SZ.asc'))
elevation_array = elevation_asc.read(1)
