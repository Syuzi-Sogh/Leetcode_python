# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]


lst = [1, 2, 3, 4, 5]
k = 2
tmp = 0
sub = 0



if k > len(lst):
    sub = k - len(lst)
    for i in range (0, len(lst) + sub):
        if k > 0:
            tmp = lst[-1]
            lst.pop()
            k = k - 1
            lst.insert(0, tmp)
else:
    for i in range (0, len(lst)):
        if k > 0:
            tmp = lst[-1]
            lst.pop()
            k = k - 1
            lst.insert(0, tmp)


print(lst)