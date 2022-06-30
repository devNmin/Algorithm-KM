"""

가위 : 1 바위 : 2 보  : 3
"""

import sys

sys.stdin = open('input/4880.txt')


def RSP(lst):
    while len(lst) != 1:

        if lst[i] == 1 and lst[i + 1] == 3:
            lst.pop(i + 1)
        elif lst[i] == 3 and lst[i + 1] == 1:
            lst.pop(i + 1)
        else:
            if lst[i] < lst[i + 1]:
                lst.pop(i)
            elif lst[i] > lst[i + 1]:
                lst.pop(i + 1)
            else:
                lst.pop(i + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input().split()))

    i = 1
    j = N
    group_1 = number_list[0:(i + j) // 2]
    group_2 = number_list[(i + j) // 2:j]
    # print(group_1, group_2)
    i = 0
    RSP(group_1)
    RSP(group_2)
    group_3 = [group_1[-1], group_2[-1]]
    RSP(group_3)

    print("#" + str(tc), number_list.index(group_3[-1]) + 1)

    # print(group_1)
    # print(group_2)
