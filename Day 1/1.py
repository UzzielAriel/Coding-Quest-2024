data = open("1.txt", "r").readlines()

cost = {}

for d in data:
	d = d.split(":")
	cost[d[0]] = 0

for d in data:
	y = d.split()
	x = d.split(":")
	if y[1] in ["Rebate", "Discount"]:
		cost[x[0]] -= int(y[2])
	else:
		cost[x[0]] += int(y[2])

temp = cost["CometAir"]
for k in cost:
	if cost[k] < temp:
		temp = cost[k]

print(temp)