# Ввод: nums = [3,0,1]
# Вывод: 2

nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)
nums.sort()

missing = 0

first = 0

for i in range(0, len(nums)):
    if first == nums[i]:
        first += 1
    else:
        missing = first
        break

print(missing)