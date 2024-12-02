def safe_asc(r, damped=False):
    for i, _ in enumerate(r):
        if i == 0:
            continue
        if r[i] <= r[i-1] or r[i] - r[i-1] > 3:
            if damped:
                return False
            return (safe_asc(r[:i-1] + r[i:], damped=True) or
                    safe_asc(r[:i] + r[i+1:], damped=True))
    return True


def safe_desc(r, damped=False):
    for i, _ in enumerate(r):
        if i == 0:
            continue
        if r[i] >= r[i-1] or r[i-1] - r[i] > 3:
            if damped:
                return False
            return (safe_desc(r[:i-1] + r[i:], damped=True) or
                    safe_desc(r[:i] + r[i+1:], damped=True))
    return True


reports = []
with open("02.input") as f:
    for line in f:
        reports.append([int(n) for n in line.split()])

sum = 0
for r in reports:
    if safe_asc(r, damped=True) or safe_desc(r, damped=True):
        sum += 1
print(sum)

sum = 0
for r in reports:
    if safe_asc(r) or safe_desc(r):
        sum += 1
print(sum)
