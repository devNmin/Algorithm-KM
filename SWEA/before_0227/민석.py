# 민석

# N : 수강생
# K : 과제를 제출한 수

import sys

sys.stdin = open("input/민석.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sub_people = list(map(int, input().split()))

    check_list = [0 for i in range(N)]
    result = ''
    for people in sub_people:
        check_list[people-1] = 1

    for check in range(len(check_list)):
        if check_list[check]:
            pass
        else:
            result += str(check+1)+' '
    print("#"+str(tc),result)


