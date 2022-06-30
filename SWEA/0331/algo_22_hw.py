import itertools

import sys

sys.stdin = open('../input/algo_22.txt')

T = int(input())
T = 2
for tc in range(1, T + 1):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    pool = []
    for i in range(N):
        pool.append(i)

    permutation = list(itertools.permutations(pool, N))

    # n = len(comb)
    # print(permutation)  # 0 2 3 1
    print(permutation)
    result = 0
    pr_result = float('-inf')
    for i in range(len(permutation)):  # 0~
        # print(permutation[i])

        percentage = 1
        print(len(permutation))
        for j in range(len(permutation[i])):
            k = permutation[i][j]
            # print(percentage)
            # print(permutation[i][j], matrix[j][k])
            pre_per = percentage
            percentage *= matrix[j][k] / 100
            cur_per = percentage

            if pre_per < cur_per:
                break
            # if percentage == 0:
            #     break

        # percentage *= matrix[i][permutation[i][j]]
        percentage *= 100
        result = round(percentage, 6)
        # print(result)
        #
        if pr_result < result:
            pr_result = result

        # print()

    # print(f'{result:0.6f}')
    print(f'#{tc} {pr_result:0.6f}')
