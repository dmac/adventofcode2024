def fill_region(g, r, c):
    target = g[r][c]
    visited = set()
    visited.add((r, c))
    q = [(r, c)]
    while len(q) > 0:
        r, c = q[0]
        q = q[1:]
        if r > 0 and g[r-1][c] == target and (r-1, c) not in visited:
            visited.add((r-1, c))
            q.append((r-1, c))
        if r < len(g)-1 and g[r+1][c] == target and (r+1, c) not in visited:
            visited.add((r+1, c))
            q.append((r+1, c))
        if c > 0 and g[r][c-1] == target and (r, c-1) not in visited:
            visited.add((r, c-1))
            q.append((r, c-1))
        if c < len(g[0])-1 and g[r][c+1] == target and (r, c+1) not in visited:
            visited.add((r, c+1))
            q.append((r, c+1))
    return visited

def area(region):
    return len(region)

def perimeter(g, region):
    p = 0
    for r, c in region:
        if r == 0 or g[r-1][c] != g[r][c]:
            p += 1
        if r == len(g)-1 or g[r+1][c] != g[r][c]:
            p += 1
        if c == 0 or g[r][c-1] != g[r][c]:
            p += 1
        if c == len(g[0])-1 or g[r][c+1] != g[r][c]:
            p += 1
    return p

def sides(g, region):
    tops = set()
    bottoms = set()
    lefts = set()
    rights = set()
    sides = 0
    for (R, C) in region:
        if (R, C) not in tops and (R == 0 or g[R-1][C] != g[R][C]):
            sides += 1
            tops.add((R, C))
            c = C
            while c > 0 and g[R][c-1] == g[R][C] and (R == 0 or g[R-1][c-1] != g[R][c-1]):
                c -= 1
                tops.add((R, c))
            c = C
            while c < len(g[0])-1 and g[R][c+1] == g[R][C] and (R == 0 or g[R-1][c+1] != g[R][c+1]):
                c += 1
                tops.add((R, c))
        if (R, C) not in bottoms and (R == len(g)-1 or g[R+1][C] != g[R][C]):
            sides += 1
            bottoms.add((R, C))
            c = C
            while c > 0 and g[R][c-1] == g[R][C] and (R == len(g)-1 or g[R+1][c-1] != g[R][c-1]):
                c -= 1
                bottoms.add((R, c))
            c = C
            while c < len(g[0])-1 and g[R][c+1] == g[R][C] and (R == len(g)-1 or g[R+1][c+1] != g[R][c+1]):
                c += 1
                bottoms.add((R, c))
        if (R, C) not in lefts and (C == 0 or g[R][C-1] != g[R][C]):
            sides += 1
            lefts.add((R, C))
            r = R
            while r > 0 and g[r-1][C] == g[R][C] and (C == 0 or g[r-1][C-1] != g[r-1][C]):
                r -= 1
                lefts.add((r, C))
            r = R
            while r < len(g)-1 and g[r+1][C] == g[R][C] and (C == 0 or g[r+1][C-1] != g[r+1][C]):
                r += 1
                lefts.add((r, C))
        if (R, C) not in rights and (C == len(g[0])-1 or g[R][C+1] != g[R][C]):
            sides += 1
            rights.add((R, C))
            r = R
            while r > 0 and g[r-1][C] == g[R][C] and (C == len(g[0])-1 or g[r-1][C+1] != g[r-1][C]):
                r -= 1
                rights.add((r, C))
            r = R
            while r < len(g)-1 and g[r+1][C] == g[R][C] and (C == len(g[0])-1 or g[r+1][C+1] != g[r+1][C]):
                r += 1
                rights.add((r, C))
    return sides

g = [[c for c in line.strip()] for line in open("12.input")]
visited = set()
regions = []
for r, row in enumerate(g):
    for c, v in enumerate(row):
        if (r, c) not in visited:
            region = fill_region(g, r, c)
            regions.append(region)
            for t in region:
                visited.add(t)

ans = 0
for region in regions:
    ans += area(region) * perimeter(g, region)
print(ans)

ans = 0
for region in regions:
    ans += area(region) * sides(g, region)
print(ans)
