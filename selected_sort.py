from random import randint

def selected_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = []
for i in range(10):
    arr.append(randint(0, 50))

print(arr)
print(selected_sort(arr))

