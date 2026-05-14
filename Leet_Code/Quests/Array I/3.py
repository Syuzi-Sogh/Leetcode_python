# Input: nums = [1,1,0,1,1,1]
# Output: 3

nums = [1,0,1,1,0,1]
max_count = 0
cntr = 0

for i in range(0, len(nums)):
    if nums[i] == 1:
        cntr += 1
        max_count = max(max_count, cntr)
    else:
        cntr = 0

print(cntr)