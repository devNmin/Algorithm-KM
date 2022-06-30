import sys

sys.stdin = open('input/square.txt')

# T = int(input())
T = 1
for test in range(1, T + 1):
    square_len = int(input())
    test_list = [list(map(int, input().split())) for _ in range(square_len)]

    for i in range(100):
        print(test_list[i])

    # print(square_len , test_list)