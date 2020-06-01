import numpy as np
import matplotlib.pyplot as plt

data = np.load('reInvent2019_track.npy')
print(data)

x = []
y = []
x2 = []
y2 = []
x3 = []
y3 = []
lineX = []
lineY = []

line = [[0.3, 2.4], [0.5, 2.2], [0.6, 1.9], [0.8, 1.7], [1.1, 1.4], [1.4, 1.3], [1.6, 1.2], [2.0, 1.1], [2.2, 1.0], [2.5, 0.9], [3.1, 0.8], [3.4, 0.8], [3.8, 0.7], [4.0, 0.7], [4.3, 0.6], [4.5, 0.6], [4.8, 0.6], [5.1, 0.5], [5.4, 0.6], [5.7, 0.7], [6.0, 0.8], [6.2, 0.8], [6.4, 1.1], [6.7, 1.4], [6.9, 1.8], [7.0, 2.0], [7.1, 2.3], [7.4, 2.6], [7.5, 3.1], [7.7, 3.5], [7.8, 3.9], [7.8, 4.4], [7.9, 4.7], [8.0, 5.1], [7.9, 5.5], [7.9, 5.7], [7.7, 5.9], [7.2, 6.0], [6.8, 6.0], [6.1, 5.9], [5.7, 5.7], [5.4, 5.6], [5.1, 5.4], [4.8, 5.0], [4.6, 4.9], [4.3, 4.7], [3.9, 4.5], [3.6, 4.3], [3.2, 4.2], [2.7, 4.1], [2.3, 4.1], [2.0, 4.1], [1.6, 4.0], [1.3, 3.9], [1.0, 3.8], [0.8, 3.7], [0.6, 3.5], [0.5, 3.2], [0.4, 3.0], [0.4, 2.6]]

for point in data:
    x.append(point[0])
    y.append(point[1])

for point in data:
    x2.append(point[2])
    y2.append(point[3])

for point in data:
    x3.append(point[4])
    y3.append(point[5])

for point in line:
    lineX.append(point[0])
    lineY.append(point[1])

fig = plt.figure()
ax = fig.add_subplot('111')
ax.plot(x, y, 'yo-')
ax.plot(x2,y2,'ro-')
ax.plot(x3,y3,'ro-')
ax.plot(lineX, lineY, 'go-')

coords = []

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print("[" + str(ix) + "," + str(iy) + "],")

    global coords
    coords.append(([ix, iy]))

    if len(coords) == 100:
        fig.canvas.mpl_disconnect(cid)

    return coords
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()