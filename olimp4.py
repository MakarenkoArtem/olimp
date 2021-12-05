_, l = [int(i) for i in input().split(" ")]
m = [int(i) for i in input().split(" ")]
c = [int(i) for i in input().split(" ")]
s = {}
for i in range(len(m)):
    if c[i] not in s.keys():
        s[c[i]] = []
    s[c[i]].append(m[i])
while 1:
    for key, values in s.items():
        if min()
print(s)