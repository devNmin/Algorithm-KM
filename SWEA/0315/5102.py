import sys

sys.stdin = open('5102.txt')

T = int(input())
T = 3
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    nodes = [list(map(int, input().split())) for _ in range(E)]
    print(V,E)
    print(nodes)

