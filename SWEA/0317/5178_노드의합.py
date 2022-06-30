import sys

sys.stdin = open('../input/5178.txt')

T = int(input())

for tc in range(1, 1 + T):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 2)]  # N+2 index 에러 피하기위해

    # tree  현재 리프 노드 값 저장
    for m in range(M):
        idx, idx_value = map(int, input().split())
        tree[idx] = idx_value

    # tree 자식 노드 합 저장
    for i in range(N - M, 0, -1):  # i => 부모 , i*2 & i*2+1 => 자식
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

    print(f'#{tc}', tree[L])
