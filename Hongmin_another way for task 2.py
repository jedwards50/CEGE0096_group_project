# Another thought to make the task 2 (example)

# easting = 454000
# northing = 87000

ELEVATION_RADIUS = 5000
source = r'.\Material\elevation\SZ.asc'

lx = 425000
ly = 75000
cell = 5

# print("header_values")
# print(header_values)

radius_cells = ELEVATION_RADIUS // cell

asc_index_x = math.floor((easting - lx) // cell)
asc_index_y = math.floor((northing - ly) // cell)
# print("asc_index_x", "asc_index_y")
# print(asc_index_x, asc_index_y)
rows_to_skip = 5 + asc_index_y - radius_cells
max_rows = radius_cells * 2 + 1
start_col = asc_index_x - radius_cells
end_col = asc_index_x + radius_cells + 1
print(start_col, end_col)
print(max_rows, rows_to_skip)


elev_arr = np.loadtxt(r'.\Material\elevation\SZ.asc', skiprows=rows_to_skip, max_rows=max_rows,
                      usecols=range(start_col, end_col))
# print(elev_arr.max())
# print(elev_arr.shape)
# print(elev_arr)
# noinspection PyArgumentList
min_elevation = elev_arr.min()
while True:
    highest_elevation = np.unravel_index(elev_arr.argmax(), elev_arr.shape)
    print(highest_elevation)
    print(elev_arr[highest_elevation[0]][highest_elevation[1]])
    h_x_index = highest_elevation[1] - radius_cells
    h_y_index = highest_elevation[0] - radius_cells

    if (h_x_index * h_x_index + h_y_index * h_y_index) < (radius_cells * radius_cells):
        bng_easting = (h_x_index + asc_index_x) * cell + lx
        bng_northing = (h_y_index + asc_index_y) * cell + ly
        print((bng_easting, bng_northing))
        break
    else:
        elev_arr[highest_elevation[0]][highest_elevation[1]] = min_elevation - 1
