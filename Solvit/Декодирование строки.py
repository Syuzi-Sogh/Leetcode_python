# Ввод: s = "3[a2[c]]"
# Вывод: "accaccacc"
from inspect import stack

s = '3[a2[c]]'

stack = []
current = ""
k = 0

for c in s:
    if c == '[':
        stack.append((current, k))
        current = ""
        k = 0

    elif c == ']':
        prev, num = stack.pop()
        current = prev + num * current

    elif c.isdigit():
        k = k * 10 + int(c)
        # print('number')

    else:
        current += c

print(current)