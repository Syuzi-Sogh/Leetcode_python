# Исходные данные: str1 = "JhonDipPeta"
# Ожидаемый результат: Dip

def find_mid(str):
    mid = len(str) // 2
    return str[mid - 1: mid + 2]


print (find_mid("JhonDipPeta"))
