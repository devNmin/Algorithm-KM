"""
    4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.


다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
"""

import sys

sys.stdin = open('input/gugansum_input.txt')

T = int(input())  # 3

for test in range(1, T + 1):
    test_N, test_M = list(map(int, input().split()))
    test_list = list(map(int, input().split()))

    max_value = test_M  # 5
    min_value = test_M * 10000
    result = []

    for i in range(test_N - test_M + 1):
        gugan_sum = 0
        for j in range(test_M):
            gugan_sum += test_list[i + j]
        if max_value < gugan_sum:
            max_value = gugan_sum

        if min_value > gugan_sum:
            min_value = gugan_sum

    print("#{}".format(test), max_value - min_value)
