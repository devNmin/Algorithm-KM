import sys

sys.stdin = open('../input/5209.txt')
"""
5209번 최소 생산 비용
"""
def dfs(product):
    global total, sum_value

    if product == N: # 결과 업뎃
        if total > sum_value:
            total = sum_value
        return

    if total <= sum_value: # 가지치기
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            sum_value += products[product][i]
            dfs(product + 1)
            visited[i] = 0
            sum_value -= products[product][i]


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    products = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sum_value = 0
    total = 987654321

    dfs(0)
    print(f'#{test_case} {total}')