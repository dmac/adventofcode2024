eqs = []
with open("07.input") as f:
    for line in f:
        v, rest = line.strip().split(":")
        nums = list(map(lambda x: int(x), rest.split()))
        eqs.append([int(v)] + nums)

def try_ops(target, nums, concat=False):
    if len(nums) == 1:
        return target == nums[0]
    if try_ops(target, [nums[0]+nums[1]] + nums[2:], concat):
        return True
    if try_ops(target, [nums[0]*nums[1]] + nums[2:], concat):
        return True
    if not concat:
        return False
    return try_ops(target, [int(str(nums[0])+str(nums[1]))] + nums[2:], concat)

ans = 0
for eq in eqs:
    if try_ops(eq[0], eq[1:]):
        ans += eq[0]
print(ans)

ans = 0
for eq in eqs:
    if try_ops(eq[0], eq[1:], concat=True):
        ans += eq[0]
print(ans)
