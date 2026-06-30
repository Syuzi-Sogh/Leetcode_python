# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

nums = [6,5,4,8]
cntr = 0
result = []

for i in range (0, len(nums)):
    for j in range(0, len(nums)):
        if nums[i] > nums[j] and (i != j):
            cntr += 1
        if j == len(nums) - 1:
            result.append(cntr)
            cntr = 0
print(result)