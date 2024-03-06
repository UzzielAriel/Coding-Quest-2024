def decode_room_code(encoded_data):
    image = []

    n = False
    f = ''
    for mode in encoded_data:
        if n:
            f = '#'
        else:
            f = '.'

        n = not n
        for x in range(int(mode)):
            image.append(f)

    return image

encoded_data = open("3.txt", "r").read().strip().split(" ")

room_code = decode_room_code(encoded_data)
t = 1
print(room_code)
for x in room_code:
    if t == 100:
        print("")
        print(x, end="")
        t = 1
        continue
    print(x, end="")
    t += 1

