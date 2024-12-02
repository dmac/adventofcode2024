def safe_asc(r):
    for i, _ in enumerate(r):
        if i == 0:
            continue
        if r[i] <= r[i-1]:
            return False
        if r[i] - r[i-1] > 3:
            return False
    return True

def safe_desc(r):
    for i, _ in enumerate(r):
        if i == 0:
            continue
        if r[i] >= r[i-1]:
            return False
        if r[i-1] - r[i] > 3:
            return False
    return True

reports = []
with open("02.input") as f:
    for line in f:
        reports.append([int(n) for n in line.split()])

sum = 0
for r in reports:
    if safe_asc(r) or safe_desc(r):
        sum += 1
print(sum)

sum = 0
for r in reports:
    for i in range(len(r)):
        rr = r[:i] + r[i+1:]
        if safe_asc(rr) or safe_desc(rr):
            sum += 1
            break
print(sum)
