with open("input.txt", "r") as file:
    data = [i.rstrip("\n") for i in file.readlines()]
with open("output.txt", "w") as file:
    a = int(data[0])
    b = int(data[1])
    i = 0
    while b < a:
        b *=2
        i += 1
    file.write(f"{i}")