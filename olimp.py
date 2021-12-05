import sys
import timeit


def solution_441():  # +
    a = [int(i) for i in input().split()]
    f = [int(i) for i in input().split()]
    s = timeit.timeit()
    a.sort()
    f.sort(reverse=True)
    for i in f:
        if a[1] >= i:
            a[1] -= i
        elif a[0] >= i:
            a[0] -= i
        else:
            a = []
            break
    if len(a):
        print("YES")
    else:
        print("NO")
    print(timeit.timeit() - s)


def solution_442():  # +
    input()
    p = [int(i) for i in input().split()]
    p.sort(reverse=True)
    a, b = [p[i] for i in range(0, len(p), 2)], [p[i] for i in range(1, len(p) - 1, 2)]
    print(abs(sum(a) - sum(b)))


def solution_443():  # -
    f = open("input.txt", "r").readlines()
    n = int(f[0])
    count = 0
    for a in range(n + 1):
        for b in range(a + 1):
            i = 1
            c = a
            while 1:
                b, c = c, c + b
                i += 1
                if b == n and i > 2:
                    count += 1
                if b >= n:
                    break
    with open("output.txt", "w") as f:
        f.write(str(count))
    # ======================================
    n = int(input())
    a = 0
    count = 0
    while a < n:
        a += 1
        for b in range(a + 1):
            i = 1
            c = a
            while 1:
                # print(b, c)
                b, c = c, c + b
                i += 1
                if b == n and i > 2:
                    count += 1
                if b >= n:
                    break
            # print("="*50)
    print(count)


def solution_444():  # -
    s = [0, 0]
    n = int(input())
    for i in range(1, 1 + n):
        if n % i == 0:
            s.append(2 ** i)
    # print(s)
    print(s[-1] - s[-2])


def solution_445():  # -
    s = set()
    for i in range(int(input())):
        a, b = input().split()
        s.add(", ".join([str(int(a) - int(a)), str(int(b) - int(a))]))
    # print(s)
    print(len(s))


def solution_446():  # -
    a = []
    for i in range(int(input())):
        a.append(input().split()[i + 1:])
    print(a)
    a = sum([len(i) for i in a])
    if a > 0:
        print(a + 1)
    else:
        print(0)


def solution_590():  # +
    f = [i.rstrip("\n") for i in open("input.txt", "r").readlines()]
    n = int(f[0])
    with open("output.txt", "w") as f:
        if n % 3:
            if n % 3 == 1:
                f.write(" ".join([str(n // 3 + 1), str(n // 3), str(n // 3)]))
            else:
                f.write(" ".join([str(n // 3 + 1), str(n // 3 + 1), str(n // 3)]))
        else:
            f.write(" ".join([str(n // 3)] * 3))

    f = [i.rstrip("\n") for i in open("input.txt", "r").readlines()]


def solution_591():  # +
    f = [i.rstrip("\n") for i in open("input.txt", "r").readlines()]
    with open("output.txt", "w") as t:
        w = {}
        for i in [int(i) for i in f[1].split()]:
            if i in w.keys():
                w[i] += 1
            else:
                w[i] = 1
        f = True
        for i in w.keys():
            if w[i] >= 4:
                t.write(str(i))
                f = False
                break
        if f:
            t.write("-1")


def solution_592():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        n = int(data[0])
        points = [int(i) for i in data[1].split()] + [0]
        distance = [int(i) for i in data[2].split()]
        V, E = [int(i) for i in data[3].split()]
        fuel = V
        for i in range(1, n):
            fuel -= E * distance[i - 1]
            if fuel < 0:
                file.write(str(i))
                break
            else:
                fuel += points[i - 1]
                if V < fuel:
                    fuel = V
        if fuel >= 0:
            file.write(str(n))


def check_593(s):
    for i in s:
        if sum(i) % 2:
            return False
    for i in range(len(s[0])):
        if sum([y[i] for y in s]) % 2:
            return False
    return True


def solution_593():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        a, b = [int(i) for i in data[0].split()]
        points = [[int(y) for y in data[i + 1].split()] for i in range(a)]
        if check_593(points):
            file.write("OK")
        else:
            a = True
            for i in range(len(points)):
                if sum(points[i]) % 2:
                    for y in range(len(points[0])):
                        points[i][y] = (points[i][y] + 1) % 2
                        if check_593(points):
                            file.write(f"{i + 1} {y + 1}")
                            a = False
                            break
                        points[i][y] = (points[i][y] + 1) % 2
                if not a:
                    break
            if a:
                file.write("Impossible")


def solution_626():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        b, a, c = [int(i) for i in data[0].split()]
        if abs(b - a) < abs(b - c):
            file.write("1")
        elif abs(b - a) > abs(b - c):
            file.write("2")
        else:
            file.write("0")


def solution_627():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        n, r = [int(i) for i in data[0].split()]
        count = 0
        for i in range(n):
            a, b = [int(i) for i in data[i + 1].split()]
            if a >= r * 2 and b >= r * 2:
                count += 1
        file.write(str(count))


def solution_628():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        c = [int(i) for i in data[1].split()]
        c.sort()
        sc = 0
        while len(c):
            if len(c) >= 3:
                sc += c[-3]
                c = c[:-3]
            else:
                break
        file.write(str(sc))


def solution_702():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        s, c, e, p = [int(i) for i in data[0].split()]
        co = 0
        if s >= p:
            co = p * c
        else:
            co = s * c
            p -= s
            co += p * e
        file.write(f"{co}")


def solution_703():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        s = [int(i) for i in data[1].split()]
        t = {}
        for i in range(len(s) // 2):
            if s[i] + s[-i - 1] not in t.keys():
                t[s[i] + s[-i - 1]] = [i + 1]
            else:
                t[s[i] + s[-i - 1]].append(i + 1)
        file.write(f"{t[max(t.keys())][0]}")


def solution_773():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        a = int(data[0])
        b = int(data[1])
        i = 0
        while b < a:
            b *= 2
            i += 1
        file.write(f"{i}")


def solution_629():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        c = {}
        n = int(data[0])
        pos = [[int(y) for y in data[i].split()] for i in range(1, n + 1)]
        list_peop = [""] * n
        day = 1
        count = 1
        while "" in list_peop:
            while day in c.values():
                s = [i for i in c.keys() if c[i] == day][0]
                c[s] = None
            for peop in range(n):
                if pos[peop][0] == day:
                    s = [i for i in c.keys() if c[i] == None]
                    if len(s):
                        c[s[0]] = pos[peop][1]
                        list_peop[peop] = str(s[0])
                    else:
                        c[count] = pos[peop][1]
                        list_peop[peop] = str(count)
                        count += 1
            day += 1
        file.write("\n".join(list_peop))


def solution_660():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        x = int(data[0])
        if x <= 28:
            file.write("2")
        elif x <= 52:
            file.write("3")
        elif x <= 77:
            file.write("4")
        else:
            file.write("5")


def solution_661():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        s = [int(i) for i in data[0].split()]
        file.write(str((10 - sum([s[i] * 3 ** (i % 2) for i in range(len(s))]) % 10) % 10))


def solution_696():  # -
    sys.stdin = open("input.txt", "r")
    t, s, x, y = [int(i) for i in input().split()]
    t -= 10
    if t < 0:
        t = 0
    sys.stdout = open("output.txt", "w")
    print(s * y + x * t)


def solution_697():  # -
    with open("input.txt", "r") as file:
        data = [i for i in file.readlines()]
    with open("output.txt", "w") as file:
        s = data[1].split()
        n = 1
        m = None
        nm = 0
        for i in data[1].split():
            if int(i) > 2:
                if m is None or m > int(i):
                    m = int(i)
                    mn = n
            n += 1
        file.write(str(mn))


def solution_732():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        x = int(data[0]) - 1
        y = int(data[1]) - 1
        file.write(str(min([(x + y) * 5, x * 20])))


def solution_733():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        d = int(data[0].split()[1])
        s = [int(i) for i in data[1].split()]
        n = 1
        for i in range(0, len(s) - 1):
            if s[i] + d <= s[i + 1]:
                n += 1
            else:
                s[i + 1] = s[i]
        file.write(str(n))


def solution_734():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        d = data[0]
        s = [0, 0, 0, 0]
        while len(d):
            if d[:1] == "0":
                d = d[1:]
                s[0] += 1
            elif d[:3] == "100":
                d = d[3:]
                s[1] += 1
            elif d[:3] == "101":
                d = d[3:]
                s[2] += 1
            elif d[:2] == "11":
                d = d[2:]
                s[3] += 1
        for i in range(len(s)):
            if s[i] == max(s):
                file.write(str(i + 2))
                break


def solution_765():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        a, b = [int(i) for i in data[0].split()]
        n = min([a, b])
        a = max([a - n, b - n])
        file.write(f"{str(n)} {str(a // 2)}")


def solution_739():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        a, b, c = [int(i) for i in data[0].split()]
        x, y, z = [int(i) for i in data[1].split()]
        if c > z:
            y -= 1
            z += 60
        s = z - c
        if b > y:
            x -= 1
            y += 60
        m = y - b
        h = x - a
        file.write(f"{h} {m} {s}")


def solution_772():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        a = int(data[0])
        n = a // 100
        a = a % 100
        n += a // 10 + a % 10
        file.write(f"{n}")


def solution_741():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        a = [int(i) for i in data[1].split()]
        d = {}
        n, m = 0, 0
        for i in range(len(a)):
            if i:
                if m < a[i]:
                    m = a[i]
                else:
                    if i - n + 1 not in d.keys():
                        d[i - n + 1] = [[n, i]]
                    else:
                        d[i - n + 1].append([n, i])
                    m = a[i]
                    n = i + 1
            else:
                n = i + 1
                m = a[i]
        if i - n + 2 not in d.keys():
            d[i - n + 2] = [[n, i + 1]]
        else:
            d[i - n + 2].append([n, i + 1])
        s = d[max(d.keys())]
        s.sort()
        file.write(f"{s[-1][0]} {s[-1][1]}")


def solution_881():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        n, a, b = int(data[0]), int(data[1]), int(data[2])
        c = True
        for i in range(n // a + 1):
            if not (n - a * i) % b and c:
                file.write(f"YES\n{i} {(n - a * i) // b}")
                c = False
                break
        if c:
            file.write("NO")


def solution_882():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        n, d = [int(i) for i in data[0].split()]
        k = [int(i) for i in data[1]]
        n = 0
        c = True
        while len(k) > 1 and c:
            n += 1
            c = False
            for i in range(1, d + 1):
                if len(k) > i and k[i]:
                    c = i
            if c:
                c = c % len(k)
                k = k[c:]
        if not c:
            file.write("-1")
        else:
            file.write(f"{n}")


def solution_884():  # -
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        n, m, k = [int(i) for i in data[0].split()]
        z = [int(i) for i in data[1].split()]
        s = 0
        h = [False] * m
        # print(z)
        for i in range(min(z), max(z) + 1):
            h = [i in z] + h[:-1]
            if h.count(True) >= k:
                h[0] = False
                s += 1
                # print(i)
            # print(i, h)
        file.write(str(s))


def solution_895():  # -
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        s = data[1]
        for i in range(int(data[0].split()[1])):
            a, b, c = data[i + 2].split()
            a, b = int(a), int(b)
            if c in s[a - 1: b]:
                s = s[:a - 1] + s[a - 1: b].replace(c, "") + s[b:]
                if not len(s):
                    break
        file.write(s)


def solution_883():  # -
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        s = {}
        for i in range(1, 1 + int(data[0])):
            if data[i].split()[0] not in s.keys():
                s[data[i].split()[0]] = []
            s[data[i].split()[0]] += data[i].split()[2:]
        for key in s.keys():
            c = list(set(s[key]))
            c = sorted(c, key=lambda x: len(x))
            n = 0
            while n < len(c):
                k = [i for i in c if c[n] == i[-len(c[n]):]]
                if len(k) > 1:
                    c = [i for i in c if i not in k[:-1]]
                else:
                    n += 1
            s[key] = c
        file.write(str(len(s)))
        for key, item in s.items():
            file.write(f"\n{key} {len(item)} {' '.join(item)}")


def solution_890():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        s = [int(i) for i in data[1].split()]
        n = 0
        while len(s):
            n += 1
            l, c, m, p = None, 0, 0, None
            for k in range(len(s)):
                i = s[k]
                if l != i:
                    c = 1
                    l = i
                else:
                    c += 1
                if c > m:
                    m = c
                    p = k - c + 1
            # print(s, p, m + p)
            # print(s[:p], s[p + m:])
            s = s[:p] + s[p + m:]
            # print(s)
        # print(n)
        file.write(f"{n}")


def solution_891():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        m = "31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31"
        n = data[1].replace(" ", ", ")
        if n in m:
            file.write("Yes")
        else:
            file.write("No")


def solution_888():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        n, a, b = int(data[0]), int(data[1]), int(data[2])
        if a <= b:
            if n >= 2 * a + b:
                file.write("1")
            elif n >= 2 * a:
                file.write("2")
            else:
                file.write("3")
        else:
            if n >= 2 * a + b:
                file.write("1")
            elif n >= b + a:
                file.write("2")
            else:
                file.write("3")


def solution_880():  # +
    with open("input.txt", "r") as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    with open("output.txt", "w") as file:
        a = int(data[0])
        if a % 10 < 5:
            a -= a % 10
        else:
            a += 10 - a % 10
        file.write(f"{a}")


def solution_735():  # +
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
