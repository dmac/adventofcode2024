from collections import Counter

def blink(stones):
    next = Counter()
    for k, v in stones.items():
        if k == 0:
            next[1] += v
        elif len(str(k)) % 2 == 0:
            s = str(k)
            l = int(s[:len(s)//2])
            r = int(s[len(s)//2:])
            next[l] += v
            next[r] += v
        else:
            next[k*2024] += v
    return next

stones = Counter(map(lambda x: int(x), open("11.input").read().split()))
for i in range(75):
    stones = blink(stones)
    if i == 24:
        print(stones.total())
print(stones.total())
