import sys

sys.stdin = open('ii.txt')

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    print(mat[i])

for i in range(N - 2):
    for j in range(1, N):
        for k in range(N - 2 - i):
            dk = k + 1
            a = mat[i + dk][j + dk]
        # i 1 3번
