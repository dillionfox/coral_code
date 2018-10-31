import numpy as np

"""
Simple monte carlo diffusion code

"""
global tmax, dt, dx
tmax = 5 ; dt = 1 ; dx = 1

def update(N, X, V, grid):
	"""
	Update all positions by ONE time step. Incorporate both velocities (V) and thermal diffusion (dX)

	"""
	dX = np.vstack((np.random.uniform(0,dx,N),np.random.uniform(0,dx,N))).T
	return [(X[i] + V[grid.query(X[i])[1]-1]/100.0 + dX[i]/100.0) for i in range(len(X)) if not np.isnan(V[grid.query(X[i])[1]-1][0])]

def run(N, X, V, grid):
	"""
	run MC

	"""
	# iterate through time steps
	for t in range(tmax)[::dt]:
		X = update(N, X, V, grid)
		print X, "\n"
	return X

if __name__ == "__main__":
	N = 3 ; X = np.zeros((N,2))
	tmax = 5 ; dt = 1 ; dx = 1
	V = np.vstack((np.ones(N),np.random.uniform(0,dx,N))).T
	grid = np.vstack((np.arange(N),np.arange(N))).T
	run(N, X, V, grid)
