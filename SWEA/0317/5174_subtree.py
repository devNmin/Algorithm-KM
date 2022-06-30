"""

E + 2
E 간선의 개수


"""
import sys

sys.stdin = open('../input/5174.txt')

T = int(input())
for tc in range(1, 1 + T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    #  부모 자식 부모 자식

    tree = [[0, 0, 0] for _ in range(E + 2)]  # L V R

    for i in range(E):
        # 0 ~ E+1
        # i * 2 # 0 2 4 => 부모
        # i * 2 + 1 # 1 3 5 =>자식
        parent, child = data[i * 2], data[i * 2 + 1]
        if tree[parent][0]:
            tree[parent][2] = child
        else:
            tree[parent][0] = child
    # print(tree)

    # 순회
    count = 0


    def in_order(node):
        global count
        if node:
            # 1. 중위 순회 => 왼쪽
            in_order(tree[node][0])
            # 2. 하고 싶은 행동
            count += 1
            # 3. 오른쪽
            in_order(tree[node][2])
        pass


    in_order(N)
    print(f'#{tc} {count}')
