# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# 1, 2, 4, 5

nums1 = [1, 2]
nums2 = [4, 5]
nums3 = nums1 + nums2
nums3.sort()
mid = len(nums3) // 2
num = 0

if len(nums3) % 2 == 1:
    print(nums3[mid])
else:
    num = nums3[mid - 1] + nums3[mid]

    print(num / 2)


