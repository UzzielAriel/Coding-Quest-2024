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

totals, t = [], 0

for route in routes:
	curr = route[0]
	for x in route:
		t += int(distances[curr.strip()][x.strip()])
		curr = x
	totals.append(t)
	t=0

print(sum(totals))