data = open("7.txt", "r").read().strip().replace("-", "").replace("Folder:", "FOLDER").replace("[", "").replace("]", "").strip().split("\n")

for i, v in enumerate(data):
	data[i] = v.split()

files = {}

free = 0
fd = []

def deletefolder(folder, a=False):
	global free
	for i, v in enumerate(files[folder]):
		try:
			if a:
				free += v[1]
				files[folder][i][1] = 0
			else:
				if "temporary" in v[0] or "delete" in v[0]:
					free += v[1]
					files[folder][i][1] = 0	
		except:
			if "D" in v[1]:
				deletefolder(v[1].split()[1].replace("D", ""), True)
			else:
				deletefolder(v[1].split()[1])

for i, v in enumerate(data):
	if v[0] == "FOLDER":
		files[v[1]] = []
		cf = v[1]
	elif ("temporary" in v[0] or "delete" in v[0]) and v[1] == "FOLDER":
		files[cf].append(v[1] + " " + v[2] + "D")
		continue
	elif v[1] == "FOLDER":
		files[cf].append(v[1] + " " + v[2])
	else:
		files[cf].append([v[0], int(v[1])])

deletefolder("0")
print(files)
print(free)