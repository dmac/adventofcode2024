from collections import defaultdict
from functools import cmp_to_key

rules = defaultdict(list)
updates = []
with open("05.input") as f:
    zz = True
    for line in f:
        line = line.strip()
        if line == "":
            zz = False
            continue
        if zz:
            a, b = line.split("|")
            rules[int(a)].append(int(b))
        else:
            updates.append([int(x) for x in line.split(",")])

def cmp(a, b):
    if b in rules[a]:
        return -1
    if a in rules[b]:
        return 1
    return 0

p1 = 0
p2 = 0
for u in updates:
    uu = sorted(u, key=cmp_to_key(cmp))
    if u == uu:
        p1 += u[len(u)//2]
    else:
        p2 += uu[len(uu)//2]
print(p1)
print(p2)
