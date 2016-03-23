import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
def update_line(num, data, line, data2, line2):
    line.set_data(data[0, :num], data[1,:num])
    line2.set_data(data2[0, :num], data2[1, :num])
    return line, line2
 
print "Read data ..."
lines = [line.strip() for line in open('data.csv')]
linesTemp = [line.strip() for line in open('cas_temp_ok.csv')]
 
pressure = []
time = []
for i, x in enumerate(lines):
    line = x.split(',')
    pressure.append(line[1])
    time.append(line[0])
 
 
temp = []
for i, x in enumerate(linesTemp):
    line = x.split(',')
    temp.append(line[1])
 
 
 
final = []
final.append(time)
final.append(pressure)
 
final2 = []
final2.append(time)
final2.append(temp)
 
 
print "Prepare data and chart..."
data = np.array(final)
data2 = np.array(final2)
 
fig = plt.figure()
# add subplot to chart
ax = fig.add_subplot(111)
# first line is red
l, = ax.plot([], [], 'r-', label="Volume")
 
# define second axis
ax2 = ax.twinx()
 
#and set line color to blue
k, = ax2.plot([], [], 'b-', label="Temperature")
 
ax.legend([l,k], [l.get_label(), k.get_label()], loc=0)
 
ax.set_xlabel("Time [seconds]")
ax.set_ylabel("Volume [liter]")
ax.set_ylim(0,150)
ax.set_xlim(0, 70)
ax2.set_ylabel("Temperature [Degrees celsius]")
ax2.set_ylim(0, 45)
ax2.set_xlim(0, 70)
plt.title('Volume and temperature in function with time.')
 
line_ani = animation.FuncAnimation(fig, update_line, 5000, fargs=(data, l, data2, k), interval=50, blit=True, repeat=False)
print "Starting drawing chart..."
plt.show()