import numpy as np
import matplotlib.pyplot as plt

data = np.load('Spain_track.npy')
print(data)

x = []
y = []
x2 = []
y2 = []
x3 = []
y3 = []
#lineX = [0,   -5, -8.6, -6, -3, -2.5, -4.7, -3.5, -2.5, 1, 3, 5, 6.5, 5.15, 7.75, 9.5, 7, 0]
#lineY = [-2, -2.5, 2.65, 4.9, 4.9, 2.25, 1.75, -0.5, -0.75, 4, 3, 0, 2, 3.75, 4.25, -0.8, -2, -2] 
lineX = []
lineY = []

line = [
    [0, -2],
    [-5, -2.5],
    [-8.6, 2.65],
    [-6, 4.9],
    [-3, 4.9],
    [-2.5, 2.25],
    [-4.7, 1.75],
    [-3.5, -0.5],
    [-2.5, -0.75],
    [1, 4],
    [3, 3],
    [5, 0],
    [6.5, 2],
    [5.15, 3.75],
    [7.75, 4.25],
    [9.5, -0.8],
    [7, -2],
    [0, -2]
]

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

plt.show()
