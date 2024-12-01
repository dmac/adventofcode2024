from collections import defaultdict

l = []
r = []
with open("01.input") as f:
    for line in f:
        (a, b) = line.split()
        l.append(int(a))
        r.append(int(b))
l.sort()
r.sort()
sum = 0
for (a, b) in zip(l, r):
    sum += abs(a - b)
print(sum)

m = defaultdict(int)
for b in r:
    m[b] += 1
sum = 0
for a in l:
    sum += a * m[a]
print(sum)
