def trailhead_metrics(g, r, c):
    summits = set()
    rating = 0
    q = [(r, c)]
    while len(q) > 0:
        r, c = q[0]
        n = g[r][c]
        q = q[1:]
        if n == 9:
            summits.add((r, c))
            rating += 1
            continue
        if r > 0 and g[r-1][c] == n + 1:
            q.append((r-1, c))
        if r < len(g)-1 and g[r+1][c] == n + 1:
            q.append((r+1, c))
        if c > 0 and g[r][c-1] == n + 1:
            q.append((r, c-1))
        if c < len(g[0])-1 and g[r][c+1] == n + 1:
            q.append((r, c+1))
    return (len(summits), rating)

g = [[int(c) for c in line.strip()] for line in open("10.input")]
scores = 0
ratings = 0
for r, row in enumerate(g):
    for c, n in enumerate(row):
        if n == 0:
            (score, rating) = trailhead_metrics(g, r, c)
            scores += score
            ratings += rating
print(scores)
print(ratings)
