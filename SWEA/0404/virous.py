import sys

sys.stdin = open('input.txt')

computer_n = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(M)]

print(graph)

vistited = [0] * (M + 1)

stack = [graph[0]]

def dfs(n):

    while stack:
        s, e = stack.pop()

        if vistited[s] == 0:
            vistited[s] = 1
        stack.append((graph[n+1]))


dfs(0)
print(sum(vistited))
