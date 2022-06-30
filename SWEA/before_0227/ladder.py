import sys

sys.stdin = open('input/ladder_input.txt')

T = 10
for tc in range(1, T + 1):
    result = 0
    test_len = int(input())
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]

    start_index = []
    start_cnt = 0

    for i in range(100):
        if ladder_matrix[99][i] == 2:
            px = i

    py = 99
    while py > 0:
        if px == 0:  # 왼쪽 벽
            if ladder_matrix[py][px + 1] != 1:
                py -= 1
            elif ladder_matrix[py][px + 1]:  # right
                ladder_matrix[py][px] = 0
                px += 1
        elif px == 99:  # 오른쪽 벽
            if ladder_matrix[py][px - 1] != 1:
                py -= 1
            elif ladder_matrix[py][px - 1]:  # left
                ladder_matrix[py][px] = 0
                px -= 1
        else:
            if ladder_matrix[py][px + 1]:  # right
                ladder_matrix[py][px] = 0
                px += 1
            elif ladder_matrix[py][px - 1]:  # left
                ladder_matrix[py][px] = 0
                px -= 1
            else:
                py -= 1

    print("#{}".format(tc), px)
