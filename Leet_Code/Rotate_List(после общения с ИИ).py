# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]


lst = [1, 2, 3, 4, 5]
k = 2
tmp = 0
sub = k % len(lst)

for i in range(0, len(lst)):
    if sub > 0:
        tmp = lst[-1]
        lst.pop()
        sub = sub - 1
        lst.insert(0, tmp)

print(lst)