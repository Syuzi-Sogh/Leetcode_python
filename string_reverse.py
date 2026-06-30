# # "ab3c2d" input
# # "abcccdd" output
#
# s = "ab3c2d"
# current = ""
# k = 0
# new_one = ""
#
# for ch in s:
#     if ch.isdigit():
#         k = int(ch)
#         current += current[-1] * (k - 1)
#     else:
#         current += ch
#
# print(current)


def Mystery(n):
    r = 0
    # for i in range(1, n - 1):
    #     for j in range(i + 1, n):
    #         for k in range(1, j):
    #             r = r + 1
    # return r
    for k in range(1, 2):
        r = r + 1
    return r


n = 1
print(Mystery(7))