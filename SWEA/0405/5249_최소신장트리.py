import sys

sys.stdin = open('5249.txt')


def make_set(x):
    p[x] = x


# x를 포함하는 집합을 찾는 연산
def find_set(x):
    if x == p[x]:
        return x
    else:  # x가 루트가 아닌 경우
        return find_set(p[x])


# x와 y를 포함하는 두 집합을 통합하는 연산
def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(E)]

    graph.sort(key=lambda x: x[-1])
    # print(graph)

    p = [i for i in range(V + 1)]

    result = 0

    # print(V, E)

    for i in range(len(graph)):
        a, b, sum_v = graph[i]
        if find_set(a) != find_set(b):
            union(a, b)
            result += sum_v
    print(f'#{tc}', result)
