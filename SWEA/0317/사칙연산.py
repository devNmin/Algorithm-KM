import sys

sys.stdin = open('../input/사칙연산.txt')

T = 10
for tc in range(1, 1 + T):
    N = int(input())
    lists = [list(input().split()) for _ in range(N)]
    lists.insert(0, [0, 0, 0, 0])
    tree = [0] * (N + 1)

    for a in range(1, len(lists)):
        if lists[a][1].isnumeric():
            tree[a] = int(lists[a][1])


    for j in range(N // 2 + 1, 0, -1):
        if lists[j][1].isnumeric():
            tree[j] = int(lists[j][1])

        if lists[j][1] == '-':
            l_n = int(lists[j][2])
            r_n = int(lists[j][3])
            if tree[l_n] != 0 and tree[r_n] != 0:
                tree[j] = int(tree[l_n]) - int(tree[r_n])

            else:
                tree[j] = int(lists[l_n][1]) - int(lists[r_n][1])
        elif lists[j][1] == '/':
            l_n = int(lists[j][2])
            r_n = int(lists[j][3])
            print(j, l_n, r_n)
            print(int(tree[l_n]), int(tree[r_n]))
            if tree[l_n] != 0 and tree[r_n] != 0:
                tree[j] = int(int(tree[l_n]) / int(tree[r_n]))

            else:
                tree[j] = int(int(lists[l_n][1]) / int(lists[r_n][1]))
        elif lists[j][1] == '+':

            l_n = int(lists[j][2])
            r_n = int(lists[j][3])

            if tree[l_n] != 0 and tree[r_n] != 0:

                tree[j] = int(tree[l_n]) + int(tree[r_n])

            else:
                tree[j] = int(lists[l_n][1]) + int(lists[r_n][1])

        elif lists[j][1] == '*':
            l_n = int(lists[j][2])
            r_n = int(lists[j][3])
            if tree[l_n] != 0 and tree[r_n] != 0:
                tree[j] = int(int(tree[l_n]) * int(tree[r_n]))

            else:
                tree[j] = int(int(lists[l_n][1]) * int(lists[r_n][1]))
    print(f'#{tc}', tree[1])
