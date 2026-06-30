def longest_increasing_streak(nums: list[int]) -> dict:
    if not nums:
        return {"length": 0}

    current_len = 1
    max_len = 1

    for i in range(1, len(nums)):
        if nums[i] >= nums[i - 1]:
            current_len += 1
        else:
            current_len = 1

        if current_len > max_len:
            max_len = current_len

    return {"length": max_len}

nums1 = [1, 3, 2, 5, 8, 4, 7]
# Выход: {"length": 3, "streak": [2, 5, 8]}
print(longest_increasing_streak(nums1))

# n 1 3 2 5 8 4 7
# i 0 1 2 3 4 5 6
# r 1 3