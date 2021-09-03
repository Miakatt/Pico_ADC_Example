import serial
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Reads the data from the serial line and plots it on a scrolling axis.

def animate(i):
    global x
    x += np.abs(np.random.randn())
    y_str = ser.readline()
    #print(y)
    y = float(y_str.decode('utf-8')) * scaleFactor
    data.append((x, y))
    ax.relim()
    ax.autoscale_view()
    ax.set_ylim([0, 3.5])
    line.set_data(*zip(*data))



ser = serial.Serial(
    port='COM3',       # Set the COM port to whatever it shows in Device Properties.
    baudrate=9600,
    timeout=1)
scaleFactor = 3.3/65535
fig, ax = plt.subplots()
x = 0
y = np.random.randn()
data = deque([(x, y)], maxlen=100)
line, = plt.plot(*zip(*data), c='green')

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()