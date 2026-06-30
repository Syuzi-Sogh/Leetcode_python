nums = [2, 2]
result = []

for i in range(len(nums)):
    if nums[i - 1] == nums[i] and (nums[i - 1] > nums[i]):
        result.append(nums[i - 1])
        nums[i] += 1
        result.append(nums[i])

    elif nums[i - 1] == nums[i] and (nums[i - 1] <= nums[i]):
        result.append(nums[i - 1])
        nums[i] -= 1
        result.append(nums[i])

print(result)