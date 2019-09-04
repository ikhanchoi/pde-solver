import numpy as np
import matplotlib.pyplot as plt

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



def Plot2d(x, t):
	plt.plot(t, x, '-')
	plt.axis([t[0], t[-1], 1.3*x.min()-0.3*x.max(), 1.3*x.max()-0.3*x.min()])

	plt.xlabel('t')
	plt.ylabel('x')
	plt.title(r'$dt=$'+'%g'%(t[1] - t[0]))
	plt.legend(['numerical'], loc='upper left')
	#plt.grid(True)

	#plt.savefig('figure.png')
	plt.show()



