import sys

sys.stdin = open("input/4466.txt")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  #
    tc_list = list(map(int, input().split()))
    tc_list.sort()
    result = 0
    max_value = 0
    for i in range(N-1, N-K-1 , -1):
        max_value += tc_list[i]
        if result <= max_value:
            result = max_value

    print(N, K, tc_list, result)
