#Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

lst1 = [2, 4, 3]
lst2 = [5, 6, 4]

result = []
cntr = 0


for i in range(len(lst1)):

    s = lst1[i] + lst2[i] + cntr
    cntr = 0

    if s >= 10:
        cntr = cntr + 1
        result.append(s % 10)
    else:
        result.append(s)

    # if (i + 1) == len(lst1):
    #     result.append(cntr)


if cntr == 1:
    result.append(cntr)

print(*result)