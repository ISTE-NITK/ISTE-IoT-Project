import matplotlib.pyplot as plt
import numpy as np
import time
#import triangulation script 

fig = plt.figure()
ax = fig.add_subplot(111)

# some X and Y data		Read these from a file? 		
x = np.arange(1000)		#numpy.fromfile(file, dtype=float, count=-1, sep='')   http://docs.scipy.org/doc/numpy/reference/generated/numpy.fromfile.html#numpy.fromfile
y = np.random.randn(1000)

li, = ax.plot(x, y)

# draw and show it
fig.canvas.draw()
plt.show(block=False)

# loop to make data update dynamically 
while True:                                 
    try:
        y[:-10] = y[10:]				#we can continuously load from the file in this loop and pass as parameters to set_ydata and set_xdata
        y[-10:] = np.random.randn(10)

        #x[:-10] = x[10:]
        #x[-10:] = np.random.randn(10)

        # set the new data
        li.set_ydata(y)
        #li.set_xdata(x)

        fig.canvas.draw()

        time.sleep(0.01)
    except KeyboardInterrupt: 
	break 