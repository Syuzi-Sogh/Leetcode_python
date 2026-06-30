tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
stack = []

result = []


for i in range(0, len(tokens)):
    if tokens[i] != "+" and tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
        stack.append(tokens[i])

    else:
        first = stack.pop()
        second = stack.pop()

        if tokens[i] == "+":
            result = first + second


print(result)