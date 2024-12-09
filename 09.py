d = []
file = True
id = 0
for c in open("09.input").read().strip():
    if file:
        for i in range(int(c)):
            d.append(id)
        file = False
        id += 1
    else:
        for i in range(int(c)):
            d.append(-1)
        file = True

def part1(d):
    i = 0
    j = len(d) - 1
    while i < j:
        while d[i] >= 0:
            i += 1
        while d[j] < 0:
            j -= 1
        if i < j:
            d[i] = d[j]
            d[j] = -1

    ans = 0
    for i, id in enumerate(d):
        if id < 0:
            break
        ans += i*id
    return ans

def find_file(d, id, j):
    while j >= 0 and d[j] != id:
        j -= 1
    if j < 0:
        return None
    end = j
    while j >= 0 and d[j] == id:
        j -= 1
    return {"id": id, "len": end - j, "idx": j + 1}

def find_space(d, l, end):
    i = 0
    while i < end:
        if d[i] >= 0:
            i += 1
            continue
        j = i + 1
        while j < end and d[j] < 0:
            j += 1
        if j - i >= l:
            return i
        i = j
    return -1

def part2(d):
    j = len(d) - 1
    while d[j] == -1:
        j -= 1
    id = d[j]
    while True:
        f = find_file(d, id, j)
        id -= 1
        if f is None:
            break
        j = f["idx"]
        i = find_space(d, f["len"], f["idx"])
        if i < 0:
            continue
        for k in range(f["len"]):
            d[i+k] = f["id"]
            d[f["idx"]+k] = -1

    ans = 0
    for i, id in enumerate(d):
        if id < 0:
            continue
        ans += i*id
    return ans

print(part1(d.copy()))
print(part2(d.copy()))
