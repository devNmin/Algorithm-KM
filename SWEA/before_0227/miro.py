import sys

sys.stdin = open('input/miro.txt')


def dfs(y, x):
    global result

    mat[y][x] = 1
    check_wall = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for (dx, dy) in check_wall:
        px = dx + x
        py = dy + y
        # 범위 체크
        if (0 <= px < N) and (0 <= py < N):
            if mat[py][px] == 0:
                dfs(py, px)
            elif mat[py][px] == 3: # 찾으면
                result = 1
                return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)] # matrix

    sx, sy = 0, 0
    result = 0

    # find start point
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                sx, sy = j, i
                break

    dfs(sy, sx)

    print("#" + str(tc), result)
