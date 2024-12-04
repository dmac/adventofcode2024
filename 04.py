def search(g, r, c, dr, dc, word):
    rows = len(g)
    cols = len(g[0])
    while r >= 0 and c >= 0 and r < rows and c < cols:
        if g[r][c] != word[0]:
            return False
        word = word[1:]
        if word == "":
            return True
        r += dr
        c += dc
    return False

def cross(g, r, c, word):
    return ((search(g, r-1, c-1, 1, 1, word) or search(g, r+1, c+1, -1, -1, word)) and
            (search(g, r-1, c+1, 1, -1, word) or search(g, r+1, c-1, -1, 1, word)))

with open("04.input") as f:
    g = [[c for c in l] for l in [l.strip() for l in f]]

word = "XMAS"
sum = 0
for r in range(len(g)):
    for c in range(len(g[0])):
        sum += 1 if search(g, r, c, 0, 1, word) else 0
        sum += 1 if search(g, r, c, 1, 0, word) else 0
        sum += 1 if search(g, r, c, 0, -1, word) else 0
        sum += 1 if search(g, r, c, -1, 0, word) else 0
        sum += 1 if search(g, r, c, 1, 1, word) else 0
        sum += 1 if search(g, r, c, -1, 1, word) else 0
        sum += 1 if search(g, r, c, 1, -1, word) else 0
        sum += 1 if search(g, r, c, -1, -1, word) else 0
print(sum)

word = "MAS"
sum = 0
for r in range(1, len(g)-1):
    for c in range(1, len(g[0])-1):
        sum += 1 if cross(g, r, c, word) else 0
print(sum)
