import sys

sys.stdin = open('input/minmax_input.txt')

T = 10
for tc in range(1, T + 1):

    test_len = int(input())
    # 100 by 100
    # 초기화
    max_left = 0
    max_right = 0
    max_col = 0
    max_row = 0

    result_max = 0
    cols = [0 for i in range(100)]
    rows = [0 for i in range(100)]

    for x in range(100):  # 100 개씩 100
        test_list = list(map(int, input().split()))  # 100

        for y in range(100):
            cols[y] += test_list[y]
            rows[x] += test_list[y]

        max_left += test_list[x]
        max_right += test_list[-1 * (x + 1)]

    for mc in cols:
        if max_col < mc:
            max_col = mc
    for mr in cols:
        if max_row < mr:
            max_row = mr

    for value in [max_left, max_right, max_col, max_row]:
        if result_max < value:
            result_max = value

    print("#{}".format(tc), result_max)