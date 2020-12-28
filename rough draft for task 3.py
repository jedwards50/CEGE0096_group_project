import geopandas as gpd
from shapely.geometry import Point, Polygon
from rtree import index
import networkx as nx

# Notice: some defination should be import from task 1 and 2 py file, if task 3 is saved independently

# 1. read the shapefile
nodes_fp = ".../nodes.shp"
nodes = gpd.read_file(nodes_fp)
# Notice: need to change the path for refer, different saved locations for material folder on computers

# 2. input the nodes with point p and differ them in colours
# Notice: might need a def here for point n
# colours for plotting in the following tasks, but also can be put in the mapplotting def part
g = nx.Graph()

g.add_node(p)
g.add_nodes_from(nodes)
g.nodes

for node in g.nodes:
    g.nodes[node]['color'] = 'green'
g.nodes[p]['color'] = 'red'

# 3. RTree for index
idx = index.Index()
for n, point in enumerate(nodes):
    idx.insert(n, point, str(n))
u = (u_x, u_y)
t = (t_x, t_y)
u_near = idx.nearesr(u, num_results=1, objects=True)
print("The nearest ITN node to the user is:", u_near)
t_near = idx.nearesr(t, num_results=1, objects=True)
print("The nearest ITN node to the highest point is:", t_near)

# Notice: t - the coordinate for the highest point in 5km buffer from the user's location, need to change according to task 2
