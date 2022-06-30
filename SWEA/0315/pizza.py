import sys

sys.stdin = open('pizza.txt')

T = int(input())
T = 1
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    M_lists = list(map(int, input().split()))
    i = 0
    while True:

        if M_lists[i] == 0:
            i = i + 1
        print(M_lists, i)
        for j in range(N):
            if i + j >= M: # 4 0 1
                if M_lists[i + j - M] != 0:
                    M_lists[i + j - M] = M_lists[i + j - M] // 2
            else:
                if M_lists[i + j] != 0:
                    M_lists[i + j] = M_lists[i + j] // 2
    # print(N, M)
    # print(M_lists)
