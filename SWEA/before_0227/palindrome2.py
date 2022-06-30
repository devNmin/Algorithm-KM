import sys

sys.stdin = open('input/회문2.txt')
#
T = 1
for test in range(1, T + 1):
    test_len = int(input())
    test_list = [input() for _ in range(100)]
    # 만약에 100이면 50번
    # 99면
    for i in range(50):
        if test_list[i] == test_list[-1*(i+1)]:
