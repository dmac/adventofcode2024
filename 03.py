import re

line = ""
with open("03.input") as f:
    line = f.read().strip()

sum = 0
muls = re.findall("mul\(\d+,\d+\)", line)
for mul in muls:
    (x, y) = re.findall("\d+", mul)
    sum += int(x)*int(y)
print(sum)

enabled = True
sum = 0
muls = re.findall("(mul\(\d+,\d+\)|do\(\)|don't\(\))", line)
for mul in muls:
    if mul == "do()":
        enabled = True
    elif mul == "don't()":
        enabled = False
    elif enabled:
        (x, y) = re.findall("\d+", mul)
        sum += int(x)*int(y)
print(sum)
