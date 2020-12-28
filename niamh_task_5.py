# TODO: Plot basemap.
# TODO: Add N arrow, scale bar, legend and colour bar for elevation range.
# TODO: Add transparent buffered elevation raster.
# TODO: Add route.
# TODO: Add starting point and end point.

# Task 5 - Map Plotting
import os
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from cartopy import crs

# Open background file.
background = rasterio.open(os.path.join('Material', 'background', 'raster-50k_2724246.tif'))

# Change colours.
palette = np.array([value for key, value in background.colormap(1).items()])
background_image = palette[background.read(1)]

# Set extent. NB: p.x and p.y reference tasks 1 and 2.
bounds = background.bounds
extent = [bounds.left, bounds.right, bounds.bottom, bounds.top]
# display_extent = [(p.x - 10000.0), (p.y - 10000.0),(p.x + 10000.0), (p.y + 10000.0)]

# Prepare the base map.
fig = plt.figure(figsize=(3, 3), dpi=300)
ax = fig.add_subplot(1, 1, 1, projection=crs.OSGB())
ax.imshow(background_image, origin='upper', extent=extent, zorder=0)
# ax.set_extent(display_extent, crs=crs.OSGB())

# Prepare the North arrow.
x, y, arrow_length = 0.05, 0.95, 0.1
ax.annotate('N', xy=(x, y), xytext=(x, y - arrow_length),
            ha='center', va='center', fontsize=5, arrowprops=dict(arrowstyle='simple', facecolor='black'),
            xycoords=ax.transAxes)

# Prepare the scale bar.

# Prepare the legend.

# Prepare the colour bar.

# Plot the base map and elements.

plt.show()

# Plot the elevation raster. #NB: This relies on the elevation raster from task 2.

#buffered_ele[0].plot(alpha=0.5)

# Plot the shortest path and start and end points. NB: shortest_path, p and end_point variables should match code
# from earlier tasks.

# shortest_path.plot(ax=ax, edgecolor='blue', linewidth=0.5, zorder=2)
# p.plot() # p is user inputted point
# end_point.plot()
