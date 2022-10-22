import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


'''
2d graph plot
2d anim plot
2d height plot
3d graph plot

2d complex number color plot
2d height color plot

direction field
integral curves
bifurcation diagram


2d plot


'''



def Plot2d_array(x, t):
	plt.plot(t, x, '-')
	plt.axis([t[0], t[-1], 1.3*x.min()-0.3*x.max(), 1.3*x.max()-0.3*x.min()])

	plt.xlabel('t')
	plt.ylabel('x')
	plt.title(r'$dt=$'+'%g'%(t[1] - t[0]))
	plt.legend(['numerical'], loc='upper left')
	#plt.grid(True)

	#plt.savefig('figure.png')
	plt.show()

def Plot2d_function(f, x):
	fig = plt.figure()
	# fig.suptitle(r'$dt=$'+'%g'%(t[1] - t[0]))
	ax = fig.add_subplot(1,1,1)

	ax.plot(x, f(x), '-')
	ax.set_xlabel('x')
	ax.set_ylabel('f(x)')
	ax.legend(['numerical'], loc='upper left')
	ax.grid(True)

	# plt.savefig('figure.png')
	plt.show()

def Plot3d_function(f, x, y):
	'''
	
	Example
	-------
		x = np.arange(-4, 4, 0.1)
		y = np.arange(-4, 4, 0.1)
		f = lambda x,y: np.sin(np.sqrt(x**2 + y**2))
		Plot3d_function(f, x, y)
	'''
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1, projection='3d')

	x, y = np.meshgrid(x, y)
	ax.plot_surface(x, y, f(x,y), rstride=1, cstride=1, cmap='hot')
	ax.set_xlabel('x')
	ax.set_xlabel('y')
	ax.set_ylabel('f(x,y)')

	plt.show()

