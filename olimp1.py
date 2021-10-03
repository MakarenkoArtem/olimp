with open("input.txt", "r") as file:
    data = [i.rstrip("\n") for i in file.readlines()]
with open("output.txt", "w") as file:
    k, s, _ = [int(i) for i in data[0].split()]
    p = [int(i) for i in data[1].split()]
    d = 1
    while 1:
        if d == s and k:
            if d % 7 != 6 and d % 7 != 0 and d not in p:
                k -= 1
            s += 1
        elif not k:
            if d % 7 != 6 and d % 7 != 0 and d not in p:
                break
        d += 1
    file.write(f"{d}")