import numpy as np
import copy

with open("06.input") as f:
    g = [[c for c in l] for l in [l.strip() for l in f]]
    p = [[0, 0], [0, 0]]
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v == "^":
                g[r][c] = "."
                p = [[r, c], [-1, 0]]

CONTINUE = 0
EXIT = 1
LOOP = 2

def step(g, p, seen=None):
    (r, c) = p[0]
    g[r][c] = "X"
    if seen is not None:
        t = (p[0][0], p[0][1], p[1][0], p[1][1])
        if t in seen:
            return LOOP
        seen.add(t)
    (r, c) = map(sum, zip(p[0], p[1]))
    if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]):
        return EXIT
    if g[r][c] == "#":
        rot = [[0, 1], [-1, 0]]
        p[1] = list(np.dot(rot, p[1]))
    else:
        p[0] = [r, c]
    return CONTINUE

g0 = copy.deepcopy(g)
p0 = copy.deepcopy(p)
while step(g0, p0) == CONTINUE:
    pass
ans = 0
for row in g0:
    for v in row:
        if v == "X":
            ans += 1
print(ans)

def try_loop(g, p, r, c):
    g[r][c] = "#"
    seen = set()
    while True:
        res = step(g, p, seen)
        if res == EXIT:
            return False
        elif res == LOOP:
            return True

ans = 0
for r, row in enumerate(g0):
    for c, v in enumerate(row):
        if g0[r][c] == "X" and r != p[0] and c != p[1]:
            if try_loop(copy.deepcopy(g), copy.deepcopy(p), r, c):
                ans += 1
print(ans)
