# даны две строки s1 и s2, создайте новую строку, добавив s2 в середину s1.

# Исходные данные: s1 = "Ault" s2 = "Kelly"
# Ожидаемый результат: AuKellylt

def create_new_str(str1, str2):
    mid = int(len(str1) // 2)
    result = str1[:mid]
    result += str2
    result += str1[mid:]
    return result

str1 = "Ault"
str2 = "Kelly"

print(create_new_str(str1, str2))