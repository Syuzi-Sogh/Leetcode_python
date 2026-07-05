t = int(input())
blocks = 0
left = 0
right = 0
result = []

for i in range(t):
    block_size = int(input())
    blocks = list(map(int, input().split()))
    tmp = float('inf')

    while blocks:
        left = blocks[0]
        right = blocks[-1]

        if left <= tmp:
            if left >= right:
                tmp = left
                blocks.pop(0)

            else:
                if right <= tmp:
                    tmp = right
                    blocks.pop(-1)
                else:
                    tmp = left
                    blocks.pop(0)
        else:
            if right <= tmp:
                tmp = right
                blocks.pop(-1)
            else:
                break

    if len(blocks) == 0:
        result.append("Yes")
    else:
        result.append("No")

for i in result:
    print(i)