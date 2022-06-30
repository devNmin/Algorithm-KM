import sys

sys.stdin = open('5248.txt')


# 유일한 원소 x를 포함하는 새로운 집합을 생성하는 연산
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
    N, M = map(int, input().split())

    lists = list(map(int, input().split()))

    p = [0] * (N + 1)
    # set 만들어주기
    for i in range(N + 1):
        make_set(i)
    # 2개씩 union
    for i in range(0, M * 2, 2):
        union(lists[i], lists[i + 1])

    result = set()
    for i in range(1, N + 1):
        result.add(find_set(i))

    print(f'#{tc}', len(result))
