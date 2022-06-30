import sys

sys.stdin = open('../input/0316_miro.txt')

for _ in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]

    # search start & end
    start_i, start_j = 0, 0

    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                start_i, start_j = i, j
                break

    queue = [(start_i, start_j)]
    matrix[start_i][start_j] = 1

    result = 0

    d_ij = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        y, x = queue.pop(0)

        for d in range(4):
            nx = x + d_ij[d][0]
            ny = y + d_ij[d][1]
            if 0 <= ny < 16 and 0 <= nx < 16:
                if matrix[ny][nx] == 0:
                    queue.append((ny, nx))
                    matrix[ny][nx] = 1
                elif matrix[ny][nx] == 3:
                    result = 1
                    break
    else:
        print(f"#{tc}", result)
