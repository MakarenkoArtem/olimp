s = [sorted([int(i) for i in input().split(" ")]) for _ in range(int(input()))]
print(sum([i[1] for i in s]))



'''print(" | ".join(['a', "b", "c", "d", "func"]))
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):

                print(" | ".join([str(i) for i in [a, b, c, d, ((a == b) <= (c == d)) or (a <= b and not c and d)]]))
'''