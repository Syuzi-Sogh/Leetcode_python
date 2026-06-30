l1 = list(map(int, (input().split())))
l2 = list(map(int, (input().split())))
result = []
if len(l1) > len(l2):
    for i in range(len(l1)):
        if len(l2) <= 0:
            result.append(l1[-1])
        else:
            result.append(l1[-1] + l2[-1])
            l1.pop()
            l2.pop()


        if result[i] >= 10:
            result[i] = result[i] - 10
            result[i - 1] += 1

else:
    for i in range(len(l2)):
        result.append(l1[-1] + l2[-1])
        l1.pop()
        l2.pop()
        if result[i] >= 10:
            result[i] = result[i] - 10
            result[i - 1] += 1


# result.reverse()
print(result)