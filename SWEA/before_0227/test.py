import sys

sys.stdin = open('input/minmax_input.txt')

T = int(input())
for test in range(1, T + 1):
    test_len = int(input())
    test_list = list(map(int, input().split()))

    print(test_len , test_list)