This code was designed to read in data from https://podaac.jpl.nasa.gov/ and 
simulate the diffusion of coral larvae. An example data set is referenced in 
the code and can be downloaded here:

https://podaac-opendap.jpl.nasa.gov/opendap/allData/oscar/preview/L4/oscar_third_deg/

USAGE: python main.py 

REQUIREMENTS: 	Python 2.7 (3.6 not tested)
		NumPy
		SciPy
		NetCDF4
		Matplotlib

If any of these dependencies are difficult to install, I recommend downloading
Miniconda (or Conda, Anaconda)  and installing everything using Pip

This code:
	1. reads ocean current velocities from a PODAAC file (NetCDF) 
	2. constructs a grid based on velocity info to determine land/ocean boundaries
	3. generates some larvae and moves them according to ocean currents and random diffusion

Variables:

N:	number of particles 

X:	2D coordinates of particles 

V:	2D velocity grid (random) 

grid: 	base of velocity vectors (2D)

dX:	update positions with small random walk steps

Vx:	update positions using nearest velocity vectors

tmax:	arbitrary time, number of steps

dt:	arbitrary time to scale number of steps

Dillion Fox, Lincoln Rehm

2018
