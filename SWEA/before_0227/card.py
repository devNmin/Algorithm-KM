"""
4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드


가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

"""

import sys

sys.stdin = open('input/card_input.txt')

T = int(input())

for tc in range(1, T + 1):
    test_len = int(input())
    test_str = input()
    result = [0 for i in range(10)]
    for i in range(test_len):
        for j in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:

            if int(test_str[i]) == j:
                result[j] += 1

    max_value = 0
    max_idx = 0
    for k in range(len(result)):
        if max_value <= result[k]:

            max_idx = k
            max_value = result[k]

    print("#{}".format(tc), max_idx, max_value)


