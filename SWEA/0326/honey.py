import sys

sys.stdin = open('../input/honey.txt')

T = int(input())
T = 1
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    # N X N
    # M : 벌통
    # C : 최대 담을 수 있는 꿀
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        j = 0
        while j < N:
            j_sum = 0
            print(N - M + 1)
            if j < N - M + 1:
                for c in range(M):  # 벌통수만큼 반복
                    # print('a', j_sum)
                    j_sum += mat[i][j + c]
                    # print('b', j_sum)
                if j_sum == C:
                    for c in range(M):
                        result.append(mat[i][j + c])
                    j += M - 1
            print(i, j, j_sum)
            j += 1
    print(result)
    rr = []

    for s in range(0, len(result), 2):
        rr.append(result[s] ** 2 + result[s + 1] ** 2)
    rr.sort()
    print(rr)
    #print(f'#{tc}', rr[-1] + rr[-2])
