import sys

sys.stdin = open('../input/5188.txt')

T = int(input())


def dfs(cci, ccj):
    global result, pre_result

    if result < pre_result:  # 도착전 조기 검진
        return
    if cci == N - 1 and ccj == N - 1:
        result = pre_result
        return
    for di, dj in dd:

        nni = cci + di
        nnj = ccj + dj
        if 0 <= nni < N and 0 <= nnj < N:
            if (nni, nnj) not in visited:
                visited.append((nni, nnj))  # 방문
                pre_result += matrix[nni][nnj]
                dfs(nni, nnj)
                pre_result -= matrix[nni][nnj]
                visited.remove((nni, nnj))


for tc in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = []

    ci, cj = 0, 0
    ni, nj = 0, 0

    dd = [(1, 0), (0, 1)]

    result = 12345678
    pre_result = matrix[0][0]
    dfs(0, 0)
    print("#{} {}".format(tc, result))
