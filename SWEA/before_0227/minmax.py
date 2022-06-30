"""
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""

import sys

sys.stdin = open('input/minmax_input.txt')

T = int(input())
for test in range(1, T + 1):
    test_len = int(input())
    test_list = list(map(int, input().split()))

    max_value = 1
    min_value = 1000000

    for i in range(test_len):
        if max_value < test_list[i]:
            max_value = test_list[i]

        if min_value > test_list[i]:
            min_value = test_list[i]

    print("#{}".format(test), max_value - min_value)

# attempt = int(input())
# for T in range(1, attempt + 1):
#     length = int(input())
#     numbers = list(map(int, input().split()))
#
#     for i in range(length - 1):
#         if numbers[i + 1] < numbers[i]:
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#
#     max_value = numbers[-1]
#
#     for i in range(length - 2):  # 이미 앞에서 리스트 맨 뒤는 제일 큰 값이기 때문에 length-2
#         if numbers[i + 1] > numbers[i]:
#           numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#
#     min_value = numbers[-2]
#
#     print("#{0}".format(T), end=" ")
#     print(max_value - min_value)

