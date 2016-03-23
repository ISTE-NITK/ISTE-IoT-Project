import matplotlib.pyplot as plt
import numpy as np
import time
#import triangulation script 

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()	

# some X and Y data		Read these from a file? 		
x = np.arange(100)		#numpy.fromfile(file, dtype=float, count=-1, sep='')
y = np.arange(100)

li, = ax.plot(x, y)

# draw and show it
fig.canvas.draw()
plt.show(block=False)

# loop to make data update dynamically 
while True:
    try:
        y[:-10] = y[10:]					# wtf is this?
        y[-10:] = np.random.randn(10)

        #x[:-10] = x[10:]
        #x[-10:] = np.random.randn(10)

        # set the new data
        li.set_ydata(y)
        #li.set_xdata(x)

        fig.canvas.draw()

        time.sleep(0.1)
    except KeyboardInterrupt: 
	break 