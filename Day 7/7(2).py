data = open("7.txt", "r").read().strip().replace("-", "").replace("Folder:", "FOLDER:").replace("[", "").replace("]", "").strip().split("\n")

for i, v in enumerate(data):
	data[i] = v.split()

files = {}
cfa = False
td = []
for i, v in enumerate(data):
	if v[0] == "FOLDER:":
		files[v[1]] = []
		cf = v[1]
		continue
	if v[1] == "FOLDER":
		files[cf].append(v[1] + " " + v[2])
		if "temporary" in v[0] or "delete" in v[0]:
			td.append(v[2])
			continue
		if cf in td:
			td.append(v[2])
			continue
	if cf in td:
		files[cf].append(int(v[1]))
		continue
	if "temporary" in v[0] or "delete" in v[0]:
		files[cf].append(int(v[1]))

free = 0
for x in files:
	for y in files[x]:
		try:
			free += y
		except:
			continue

print(free)