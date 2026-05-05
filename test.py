from random import randint

def binary_search(arr, low, high, key):
    if high > low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            binary_search(arr, mid + 1, high, key)


arr=[]
for i in range(10):
    arr.append(randint(0, 10))

arr.sort()
print(arr)
print(binary_search(arr,0, 10, 5))