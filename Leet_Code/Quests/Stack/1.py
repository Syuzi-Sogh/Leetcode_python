# Input:
# target = [1, 3]
# n = 3
#
# Output:
# ["Push", "Push", "Pop", "Push"]

target = [2, 3, 4]
n = 4
s = []
result = []

for i in range(1, n + 1):
    s.append(i)
    result.append("Push")

    if s == target:
        break

    if i not in target:
        s.pop()
        result.append("Pop")




print(result)