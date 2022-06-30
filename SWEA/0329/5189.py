import sys

sys.stdin = open('../input/5189.txt')

T = int(input())


def dfs(s):
    global result, min_result
    if len(stack) == N - 1:
        for i, j in stack:
            result += Battery[i][j]

        result += Battery[s][0]

        if result < min_result:
            min_result = result

        result = 0
        return

    for k in range(1, N):
        if not visited[k]:
            stack.append((s, k))
            visited[k] = 1
            dfs(k)
            stack.pop()
            visited[k] = 0


for tc in range(1, T + 1):
    N = int(input())  # 3 ~ 10
    Battery = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 0
    min_result = 100 * 10
    stack = []
    dfs(0)

    print(f'#{tc}', min_result)
