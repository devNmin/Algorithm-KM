import itertools
import sys

sys.stdin = open('../input/algo_22.txt')

def dfs(idx, end, result):
    global max_result
    if idx == end:
        if result > max_result:
            max_result = result
        return
    if result <= max_result:
        return
    for i in range(N):
        if not visit[i]:
            new_result = result * matrix[idx][i] * 0.01
            visit[i] = 1
            dfs(idx + 1, end, new_result)
            visit[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N

    max_result = float('-inf')

    dfs(0, N, 1)
    answer = format(max_result * 100, '.6f')
    print(f'#{tc}', answer)
