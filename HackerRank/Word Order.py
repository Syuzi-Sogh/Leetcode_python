number = int(input())
letters = ""
smth = []
for_similar = []
count = 0


for i in range(number):
    letters = input()
    smth.append(letters)

for i in range(len(smth)):
    if smth[i] not in for_similar:
        for_similar.append(smth[i])

print(len(for_similar))

for word in for_similar:
    count = smth.count(word)
    print(count, end=" ")
