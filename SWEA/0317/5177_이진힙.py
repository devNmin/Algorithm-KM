import sys

sys.stdin = open('../input/5177.txt')

T = int(input())


def heap(n):
    tree.append(n)
    idx = len(tree) - 1
    while idx:  # idx 0이 될때까지
        if tree[idx] < tree[idx // 2]:  # 자식< 부모 => 부모가 더클경우
            tree[idx], tree[idx // 2] = tree[idx // 2], tree[idx]
        idx //= 2


for tc in range(1, 1 + T):
    N = int(input())

    data = list(map(int, input().split()))
    tree = [0]  # 여기에 추가

    # heap
    for d in data:
        heap(d)

    # sum
    next_idx = N
    result = 0
    while True:
        # 마지막은 포함 X
        next_idx = next_idx // 2
        if next_idx == 0: # 0이면 그만더해
            break
        else:
            result += tree[next_idx]

    print(f'#{tc}', result)
