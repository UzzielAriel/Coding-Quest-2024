lines = open("7.txt", "r").readlines()
files = {}

for x in lines:
    if "Folder" in x:
        files[x.split()[1]] = []

for y in files.keys():
    for x in lines:
        if "Folder: " + y in x:
            t = lines.index(x)+1
            while True and t < len(lines):
                if lines[t].split()[0] == "-":
                    files[y].append(lines[t][1:])
                else:
                    break
                t += 1

todelete = []
for x in files:
    for y in files[x]:
        if "temporary" in y or "delete" in y:
            todelete.append(y.split()[1:])

freed = 0

for x in todelete:
    if x[1] == "[FOLDER":
        folderidx = x[2].replace("]", "")
        if files[folderidx]:
            for y in files[folderidx]:
                j = y.split()
                if "[" in j[2]:
                    todelete.append(y.split()[1:])
                    continue
                freed += int(j[2])
            files[folderidx] = 0 


for x in files:
    if files[x]:
        for y in files[x]:
            if "temporary" in y or "delete" in y:
                try:
                    freed += int(y.split()[2])
                except:
                    continue

print(freed)