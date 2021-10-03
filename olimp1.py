with open("input.txt", "r") as file:
    data = [i.rstrip("\n") for i in file.readlines()]
with open("output.txt", "w") as file:
    t, s, x, y = [int(i) for i in data[0].split()]
    t -= 10
    if t < 0:
        t = 0
    file.write(str(s * y + x * t))
