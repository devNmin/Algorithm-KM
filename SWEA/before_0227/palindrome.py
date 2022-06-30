import sys

sys.stdin = open('input/회문2.txt')


T = 3
for test in range(1, T + 1):
    tc = int(input())
    str_list = [list(input()) for _ in range(100)]

    A = 1
    N = 100
    while N and A:
        # print(N)
        count = 0
        for i in range(100):

            for j in range(100-N+1): # 10 01<>-1 -2

                for k in range(N//2):
                    if str_list[i][j+k] == str_list[i][j+N//2-k-1]:
                        count += 1

                if count == N//2:
                    N = 0
                    A = 0
        N -= 1
    print(count//2)


            # for i in range(N):
            #     for j in range(N):
            #         if i < j:
            #             str_list[i][j], str_list[j][i] = str_list[j][i], str_list[i][j]
            #
            #     count = 0
            #     for j in range(int(N / 2)):
            #         if str_list[i][j] == str_list[i][-1 * (j + 1)]:
            #             count += 1
            #
            #         if count == int(N / 2) - 1:
            #             print(f"#{test} {str_list[i]}")
            #             A = 0

# 4861 회문

# T = 1
# for tc in range(1, T + 1):
#     N = 100
#     M = 100
#     alpha = [input() for _ in range(N)]
#
#     A = 0
#     ans = ''
#     while M > 1:
#         half = M // 2
#         if A:
#             break
#         for i in range(N):
#             if A:
#                 break
#             for j in range(N-M+1):
#                 # 가로줄이 회문인가?
#                 check = 0
#                 if j <= N - M+1:
#                     for k in range(half):
#                         # 회문인지 검증
#                         if alpha[i][j + k] == alpha[i][j + M - k - 1]:
#                             check += 1
#
#                         # 회문 발견, 문제 조건중 회문은 반드시 하나만 있다.
#                         # 회문을 발견한 index와 가로줄인지 여부를 저장(가로의 경우 is_row=True)
#                         if check == half:
#                             A = 1
#                             break
#
#                 # 세로줄이 회문인가?
#                 check = 0
#                 if i <= N - M+1:
#                     if A:
#                         break
#                     for k in range(half):
#                         if alpha[i + k][j] == alpha[i + M - k - 1][j]:
#                             check += 1
#
#                         if check == half:
#                             A = 1
#                             break
#
#
#         M -= 1
#
#
#     print(f"#{T} {ans}")
