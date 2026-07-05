from collections import deque

d = deque()

number_of_operators = int(input())
# operators = []
operators = ""
numbers = []

# for i in range(number_of_operators):
#     operators.append(input())



for i in range(number_of_operators):
    operators = input()
    # numbers = [int(word) for word in operators.split() if word.isdigit()]
    numbers = operators.split()


    if numbers[0] == "popleft":
        d.popleft()

    if numbers[0] == "pop":
        d.pop()

    if numbers[0] == "append":
        d.append(int(numbers[1]))

    if numbers[0] == "appendleft":
        d.appendleft(int(numbers[1]))

print(*d)