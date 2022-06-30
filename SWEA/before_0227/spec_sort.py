# 2.4843 특별한 정렬

import sys

sys.stdin = open('input/spec_input.txt')

T = int(input())


def my_sorted_bubble(values):
    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]


for tc in range(1, T + 1):

    _ = int(input())
    number_list = list(map(int, input().split()))

    result_str = ''
    my_sorted_bubble(number_list)

    # 특별히 정렬된 숫자를 10개까지 출력한다.
    for n in range(5):  # i: 0, 1, 2, 3, 4

        # 뒤에서 부터 하나씩 -1 -2 ...
        result_str += str(number_list[-1 * (n + 1)]) + ' '
        # 앞에서 부터 하나씩 0 1 2 ...
        result_str += str(number_list[n]) + ' '

    # result_str += str(test_list[-1 * (i + 1)]) + ' ' + str(test_list[i]) + ' '
    print(f"#{tc}", result_str)
