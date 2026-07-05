from collections import OrderedDict

words = OrderedDict()
for _ in range(int(input())):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(" ".join(map(str, words.values())))