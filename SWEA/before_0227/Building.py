# 0209 algo-homework

import sys

sys.stdin = open('input/Building_input.txt')

# T = 10
#
# for test in range(1, T + 1):
#     result = 0
#     test_len = int(input())
#     test_list = list(map(int, input().split()))
#     result_list = []
#
#     for i in range(2, test_len - 2):
#         value_l_1 = test_list[i] - test_list[i - 1]
#         value_l_2 = test_list[i] - test_list[i - 2]
#         value_r_1 = test_list[i] - test_list[i + 1]
#         value_r_2 = test_list[i] - test_list[i + 2]
#         result_list = [value_l_1, value_l_2, value_r_1, value_r_2]
#
#         min_v = min(result_list)
#         if min_v > 0:
#             result = result + min_v
#     print("#{}".format(test), result)

T = 10

for test in range(1, T + 1):

    test_len = int(input())
    test_list = list(map(int, input().split()))
    # result_list = []
    result = 0
    i = 2
    while i < test_len - 2:
        result_list = test_list[i - 2:i + 3]  # 5개씩
        result_list.pop(2)
        max_value = result_list[0]

        for j in range(4):
            if max_value < result_list[j]:
                max_value = result_list[j]

        differ = test_list[i] - max_value

        if differ > 0:
            result = result + differ
            i += 2
        i += 1
    print(f"#{test} {result}")
