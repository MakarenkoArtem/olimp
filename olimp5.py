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