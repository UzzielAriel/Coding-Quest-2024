import numpy as np
import matplotlib.pyplot as plt
import math
 
fig = plt.figure()
ax = plt.axes(projection='3d')

d = lambda x1, x2, y1, y2, z1, z2: math.sqrt((x1-x2)**2 + (y1-y2)**2  + (z1-z2)**2)
f = open("4.txt", "r").readlines()[1:]

t = 9999999999999999999
p = ""

for i in f:
	for j in f:
		if i == j:
			continue
		s1 = i.split()
		s2 = j.split()
		
		v1 = list(map(float, [x for x in s1[-3:]]))
		v2 = list(map(float, [x for x in s2[-3:]]))
		
		cd = d(v1[0], v2[0], v1[1], v2[1], v1[2], v2[2])

		if cd < t:
			t = cd

print(t)

for i in f:
	s1 = i.split()
	v1 = list(map(float, [x for x in s1[-3:]]))
	ax.scatter(v1[0], v1[1], v1[2])

plt.show()