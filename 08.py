from collections import defaultdict

m = defaultdict(list)
rows = 0
cols = 0
with open("08.input") as f:
    for r, line in enumerate(f):
        rows += 1
        for c, s in enumerate(line.strip()):
            if r == 0:
                cols += 1
            if s != ".":
                m[s].append((r, c))

def in_bounds(p):
    r, c = p[0], p[1]
    return (r >= 0 and r < rows and
            c >= 0 and c < cols)

def anti_pair(a, b):
    dr = b[0] - a[0]
    dc = b[1] - a[1]
    x = (a[0]-dr, a[1]-dc)
    y = (b[0]+dr, b[1]+dc)
    nodes = []
    if in_bounds(x):
        nodes.append(x)
    if in_bounds(y):
        nodes.append(y)
    return nodes

def anti_any(a, b):
    dr = b[0] - a[0]
    dc = b[1] - a[1]
    antis = set()
    antis.add(a)
    p = a
    while True:
        p = (p[0]-dr, p[1]-dc)
        if not in_bounds(p):
            break
        antis.add(p)
    p = a
    while True:
        p = (p[0]+dr, p[1]+dc)
        if not in_bounds(p):
            break
        antis.add(p)
    return antis

def count_antis(anti_fn):
    antis = set()
    for k, ps in m.items():
        for i in range(len(ps)):
            for j in range(i+1, len(ps)):
                nodes = anti_fn(ps[i], ps[j])
                antis = antis.union(nodes)
    return len(antis)


print(count_antis(anti_pair))
print(count_antis(anti_any))
