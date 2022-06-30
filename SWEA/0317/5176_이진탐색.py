import sys

sys.stdin = open('../input/5176.txt')

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())

    value = 1
    tree = [0] * (N + 1)


    def in_order(node):
        global value
        if node <= N:
            # i : 1 2
            # i*2: 2 4
            # i*2 +1 : 3 5
            in_order(node * 2)

            # 여기에 하고 싶은거
            tree[node] = value
            value += 1
            # 오른쪽

            in_order(node * 2 + 1)
        pass


    in_order(1)

    print(f'#{tc} {tree[1]} {tree[N // 2]}')
