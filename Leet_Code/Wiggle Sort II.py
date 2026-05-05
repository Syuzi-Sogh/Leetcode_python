# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

#my_code

arr = [1, 2, 3, 4, 5]
tmp = 0
new_arr = []
size = len(arr) // 2

for i in range(1, len(arr)):
    for j in range(0, i):
        if arr[j] > arr[i]:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp


first_half = arr[:size] #min
second_half = arr[size:] #max


max_first_half = 0
max_second_half = 0




for i in range(1, len(first_half) + 1):
    new_arr.append(first_half[-i])
    new_arr.append("<")


    new_arr.append(second_half[-1])
    second_half.pop()
    new_arr.append(">")


print(*new_arr)




