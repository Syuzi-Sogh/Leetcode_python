# Input: nums = [1,2,2,4]
# Output: [2,3]

nums = [1, 1, 2]
result = []
number = 1
result_ = []
index = 0


nums_set = set(nums)

# nums.count(number) - output: 2
# print(nums.count(number))

for i in range(len(nums)):

    if nums.count(number) == 0:
        number += 1
    else:
        index = i
        print(index)


# time-limit, but working
#
# nums_set = set(nums)
#
# for i in range(len(nums)):
#     number = 1
#     for j in range(len(nums)):
#
#         if number not in nums_set:
#             if i < 1:
#                 result.append(number)
#                 number += 1
#
#         else:
#             number += 1
#
#         if nums[i] == nums[j] and i != j:
#             if len(result_) == 1:
#                 break
#             result_.append(nums[i])
#
#
#
# print(result_ + result)


# for i in range(0, len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[-1] <= nums[0]:
#             isHigher = False
#         if nums[i] == nums[j]:
#             index = i
#             result.append(nums[i])
#             result.append(nums[j])
#
# if isHigher == False and (result[1] - 1 != 0 or result[0] - 1 != 0):
#     result[0] -= 1
#
# else:
#     result[1] += 1




# doesn't work with case [2, 2], bcs it's can't understand in wich way it's oredered
#
# for i in range(len(nums)):
#     if nums[i - 1] == nums[i]:
#         result.append(nums[i - 1])
#         nums[i] += 1
#         result.append(nums[i])
#
#     elif nums[i - 1] == nums[i] and (nums[i - 1] <= nums[i]):
#         result.append(nums[i - 1])
#         nums[i] -= 1
#         result.append(nums[i])


