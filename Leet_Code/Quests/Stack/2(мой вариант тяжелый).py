tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

save_point = []
result = 0

for i in range(len(tokens)):
    if tokens[i] != "+" and tokens[i] != "*" and tokens[i] != "/" and tokens[i] != "-":
        save_point.append(tokens[i])

    else:
        if tokens[i] == "+":
            result = int(save_point[-1]) + int(save_point[-2])
            save_point.pop()
            save_point.pop()
            save_point.append(result)

        if tokens[i] == "*":
            result = int(save_point[-1]) * int(save_point[-2])
            save_point.pop()
            save_point.pop()
            save_point.append(result)

        if tokens[i] == "/":
            if int(save_point[-2]) > int(save_point[-1]):
                result = int(int(save_point[-2]) / int(save_point[-1]))
                save_point.pop()
                save_point.pop()
                save_point.append(result)
            #     result = int(int(save_point[-2]) / int(save_point[-1]))
            #     save_point.pop()
            #     save_point.pop()
            #     save_point.append(result)
            #
            # else:
            #     result = int(int(save_point[-1]) / int(save_point[-2]))
            #     save_point.pop()
            #     save_point.pop()
            #     save_point.append(result)

        if tokens[i] == "-":
            result = int(save_point[-1] - int(save_point[-2]))
            save_point.pop()
            save_point.pop()
            save_point.append(result)

print(result)