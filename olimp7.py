_, s = input(), input()
print(sum([len([1 for y in range(i, len(s)) if (ord(s[i]) < ord(s[y]))]) for i in range(0, len(s))]))