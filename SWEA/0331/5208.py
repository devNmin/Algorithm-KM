import sys

sys.stdin = open('../input/5208.txt')
"""
5208번 전기버스2
"""
def dfs(n):
    global charge, result

    if n >= len(station):
        if result >= charge:
            result = charge
        return

    if result <= charge:
        return

    for i in range(n+station[n], n, -1):
        charge += 1
        dfs(i)
        charge -= 1


T = int(input())

for tc in range(1, T + 1):
    station = list(map(int, input().split()))
    N = station[0]
    result = 987654321
    charge = 0
    dfs(1)

    print(f'#{tc} {result-1}')