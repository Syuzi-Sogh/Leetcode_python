# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
from collections import deque

root = [3, 9, 20, 0, 0, 15, 7]
result = []
queue = deque([root])

while queue:
    level_sum = 0
    level_count = len(queue)

    for _ in range(level_count):