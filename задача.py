# "ab3c2d" input
# "abcccdd" output

s = "ab3c2d"
current = ""
k = 0
new_one = ""

for ch in s:
    if ch.isdigit():
        k = int(ch)
        current += current[-1] * (k - 1)
    else:
        current += ch

print(current)
