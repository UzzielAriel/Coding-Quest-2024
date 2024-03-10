import matplotlib.pyplot as plt
import numpy as np

routes = open("5(2).txt", "r").readlines()
routes = [["base"] + x.split("->")[1:] for x in routes]

data = open("5.txt", "r").readlines()
stations = data[0].split()
data = list(map(lambda x: x.strip().split(), data))[1:]

# distances = {x: 0 for x in stations}
# for x in data:
# 	distances[x[0]] = {s: l for s, l in zip(stations, x[1:])}

# Done in one line below
distances = {x[0]: {s: l for s, l in zip(stations, x[1:])} for x in data}

totals, t, d, s = [], 0, [], []

for route in routes:
	curr = route[0]
	for x in route:
		t += (lambda x: [d.append(x), x])(int(distances[curr.strip()][x.strip()]))[1]
		curr = x
	(lambda s: [totals.append(t), s.append(t)])(s)
	t=0

# Visualisation for the distance of all the routes calculated on a bar chart + scatter diagram + outputting the result for the challenge in console
(lambda d: [plt.subplot(2, 2, 1), plt.scatter(d, [np.random.rand() for z in range(len(d))]), plt.subplot(2, 2, 2), plt.bar([f"{x}" for x in range(len(s))], s), plt.show(), print(sum(totals))])(d)