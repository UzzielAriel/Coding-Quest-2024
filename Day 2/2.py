def form(ip):
    d = '.'.join(str(int(ip[x:x+2], 16)) for x in range(0, len(ip), 2))
    return d

s = 0
p = 0

f = open("2.txt", "r")

for z in f:
    l = int(z[4:8], 16)
    a = form(z[24:32])
    b = form(z[32:40])

    if a.startswith("192.168.") or b.startswith("192.168."):
        s += l
    elif a.startswith("10.0.") or b.startswith("10.0."):
        p += l

print(f"{s}/{p}")