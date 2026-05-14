# Исходные данные: str1 = "James"
# Ожидаемый результат: Jms

str1 = "James"

result = []

for i in range(len(str1)):
    if i % 2 == 0:
        result += str1[i]

print(*result)