# Input: gas = [5, 1, 2, 3, 4], cost = [4, 4, 1, 5, 1]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.


gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]
tank = 0
start = 0

if sum(gas) < sum(cost):
    print("-1")

for i in range(len(gas)):
    tank += gas[i] - cost[i]

    if tank < 0:
        start = i + 1
        tank = 0
print(start)