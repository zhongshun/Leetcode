nums = [2,7,11,15]
target = 9
seen = {}
for index, num in enumerate(nums):
    res = target - num
    if res in seen:
        print (seen[res],index)
    else:
        seen[num] = index
