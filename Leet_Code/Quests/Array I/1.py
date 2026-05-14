# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

nums = [2, 5, 1, 3, 4, 7]
mid = 3

x = nums[:mid]
y = nums[mid:]

answer = []


for i in range(mid):
    answer.append(x[i])
    answer.append(y[i])

print(answer)