import numpy as np
from scipy import spatial
from hydro_tools import load_netcdf
from hydro_tools import random_walk

"""
Hydrology simulation code

"""

# load data. Currently not using "land_grid"
fil = 'oscar_vel1992.nc.gz.nc4'
lat,lon,Vx,Vy,land_grid = load_netcdf.load(fil)

# set up grid
dx, dy = np.meshgrid(lat,lon)
grid = np.array(zip(dx.flatten(), dy.flatten())[:])

# Convert grid to KD-Tree
tree = spatial.KDTree(grid)

# velocity grid (first time point velocities only!)
V = np.array(zip(Vx[0][0].flatten(), Vy[0][0].flatten())[:])

# randomish starting point. Not a great one since it's near land
start = 502835

# run MC. N is number of larvae, X is initial positions
N = 4 ; X = np.array([grid[start] for _ in range(N)])
random_walk.run(N, X, V, tree)
