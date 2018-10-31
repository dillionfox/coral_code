import numpy as np

def plot_grid(grid):
	"""
	Simple plotting function to demonstrate proof of concept: 
	1's correspond to land, 0's correspond to ocean

	"""
	import matplotlib as mpl ; mpl.use('Agg')
	import matplotlib.pyplot as plt
	plt.imshow(grid)
	plt.savefig('grid.png')
	return None

def load(fil):
	"""
	Load the NetCDF file and save data as numpy arrays
	Return: grid, latitude, longitude, velocities

	"""
	import netCDF4 as nc

	# unpack file using netCDF4
	data = nc.Dataset(fil, 'r')
	
	# latitude
	lat = np.array(data.variables['latitude'][:])
	
	# longitude
	lon = np.array(data.variables['longitude'][:])
	
	# extract velocity data
	u = np.array(data.variables['u'][:])
	v = np.array(data.variables['v'][:])
	
	# test set
	u00 = u[0][0] ; v00 = v[0][0]
	
	# placeholders -- UPDATE !
	V = np.vstack((u,v)).T

	# make arbitrary grid
	grid = np.zeros((u00.shape))
	
	# all grid points overlapping land are set to 1
	grid[np.where(np.isnan(u00))] = 1

	return lat,lon,u,v,grid

if __name__ == "__main__":
	# import netCDF file
	fil = 'oscar_vel1992.nc.gz.nc4'
	lat,lon,u,v,grid = load(fil)
	plot(grid)
