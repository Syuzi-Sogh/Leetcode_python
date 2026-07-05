t = int(input())
result = []

for i in range(t):
    block_size = int(input())
    blocks = list(map(int, input().split()))
    tmp = float('inf')
    left_idx = 0
    right_idx = len(blocks) - 1
    possible = True

    while left_idx <= right_idx:
        left = blocks[left_idx]
        right = blocks[right_idx]

        if left <= tmp:
            if left >= right:
                tmp = left
                left_idx += 1
            else:
                if right <= tmp:
                    tmp = right
                    right_idx -= 1
                else:
                    tmp = left
                    left_idx += 1
        else:
            if right <= tmp:
                tmp = right
                right_idx -= 1
            else:
                possible = False
                break

    if possible:
        result.append("Yes")
    else:
        result.append("No")

for r in result:
    print(r)