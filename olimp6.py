n, k = int(input()), int(input())
s= [int(input()) for i in range(n)]
c = {}
for i in range(n - k, 0, -1):
    c[sum([s[i] - s[i - 1] for y in range(i, i + k)])] = i
print(c[min(c.keys())])
