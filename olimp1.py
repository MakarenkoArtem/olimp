a, b, c, d, n = [int(input()) for i in range(5)]
days = n * 7
n = days // (a + b)
n = a * n * c + b * n * d
if days % (a + b):
    if days % (a + b) > a:
        n += c * a + d * (days % (a + b) - a)
    else:
        n += c * (days % (a + b))
print(n)



'''import re

num = {"ones": ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
       'tens': ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
       'hunds': ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
       'thous': ["", "M", "MM", "MMM"]}
with open(input(), "r", encoding='utf-8') as file:
    data = " ".join([i.rstrip("\n") for i in file.readlines()]) + " "
    result = list(
        set([i[1:-1] for i in re.findall(r' \d{1,4} ', data)] + [i[1:-2] for i in re.findall(r' \d{1,4}, ', data)] + [i[1:-2] for i in re.findall(r' \d{1,4}. ', data)]))
    result = [int(i) for i in result]
    result.sort(reverse=True)
    for a in result:
        t = num['thous'][a // 1000] + num['hunds'][a % 1000 // 100] + num['tens'][a % 100 // 10] + num['ones'][a % 10]
        data = data.replace(" " + str(a) + " ", " " + t + " ")
        data = data.replace(" " + str(a) + ". ", " " + t + ". ")
        data = data.replace(" " + str(a) + ", ", " " + t + ", ")
print(data[:-1])
'''