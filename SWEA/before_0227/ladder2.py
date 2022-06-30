import sys

sys.stdin = open('input/ladder2.txt')

T = 10
for tc in range(1, T + 1):
    result = 0
    test_len = int(input())
    ladder_matrix = [list(map(int, input().split())) for _ in range(100)]

    start_index = []
    start_cnt = 0

    for i in range(100):
        if ladder_matrix[0][i] == 1:
            start_index.append(i)
            start_cnt += 1
    #print(start_index)

    min_result = 10000
    min_idx = 0
    for x in start_index:
        result = 0
        px = x
        py = 0

        # print("***********",x)
        while py < 99:

            if 0 < px < 99:
                if ladder_matrix[py][px + 1]:
                    # print("asdasd",px, py)
                    while ladder_matrix[py][px + 1] == 1 and px < 98:
                        # print(px, py)

                        px += 1
                        result += 1
                    py += 1
                    result += 1
                elif ladder_matrix[py][px - 1] and px > 1:
                    while ladder_matrix[py][px - 1] == 1:
                        px -= 1
                        result += 1
                    py += 1
                    result += 1
                else:
                    py += 1
                    result += 1
            else:
                if px == 0 and ladder_matrix[py][px + 1]:
                    while ladder_matrix[py][px + 1] == 1:
                        px += 1
                        result += 1
                    py += 1
                    result += 1
                elif px == 99 and ladder_matrix[py][px - 1]:
                    while ladder_matrix[py][px - 1] == 1:
                        px -= 1
                        result += 1
                    py += 1
                    result += 1
                else:
                    py += 1
                    result += 1
        else:

            if min_result > result:
                min_result = result
                min_idx = x

    print("#{}".format(tc), min_idx)
