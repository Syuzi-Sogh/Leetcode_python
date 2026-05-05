# написать количество дней, которое придется ждать до теплее температуры
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Сейчас j у тебя не зависит от текущего i, поэтому ты сравниваешь не “вперёд от i”, а почти случайные позиции массива.

temp = []

cntr = 0
new_arr = []


for i in range(0, len(temp)):
    for j in range(i + 1, len(temp)):
        if temp[i] < temp[j]:
            cntr = cntr + 1
            new_arr.append(cntr)
            cntr = 0
            break


        elif temp[i] > temp[j]:
            cntr = cntr + 1

    else:
        new_arr.append(0)


print(new_arr)
