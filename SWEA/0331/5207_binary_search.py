import sys

sys.stdin = open('../input/5207.txt')

T = int(input())

for tc in range(1, T + 1):
    answer = 0
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    result = 0
    for b in B:
        # 초기설정
        l, r = 0, N - 1
        lr_flag = 0
        while True:
            if l > r:
                break
            m = (l + r) // 2
            if b == A[m]: # b => 우리가 찾고자하는
                result += 1
                break
            elif b > A[m]:  # 우
                if lr_flag == 2:
                    break
                else:
                    l = m + 1
                    lr_flag = 2
            elif b < A[m]:  # 좌
                if lr_flag == 1:
                    break
                r = m - 1
                lr_flag = 1

    print(f'#{tc}', result)
