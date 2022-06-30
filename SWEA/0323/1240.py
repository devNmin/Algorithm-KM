import sys

sys.stdin = open('../input/1240.txt')

# 암호코드 reverse
reversed_number = [
    ['1', '0', '1', '1', '0', '0', '0'], # 0
    ['1', '0', '0', '1', '1', '0', '0'], # 1
    ['1', '1', '0', '0', '1', '0', '0'], # 2
    ['1', '0', '1', '1', '1', '1', '0'], # 3
    ['1', '1', '0', '0', '0', '1', '0'], # 4
    ['1', '0', '0', '0', '1', '1', '0'], # 5
    ['1', '1', '1', '1', '0', '1', '0'], # 6
    ['1', '1', '0', '1', '1', '1', '0'], # 7
    ['1', '1', '1', '0', '1', '1', '0'], # 8
    ['1', '1', '0', '1', '0', '0', '0'], # 9
]

T = int(input())

for tc in range(1, 1 + T):
    # N : 세로
    # M : 가로
    N, M = map(int, input().split())
    # 7* 8 = 56
    matrix = [list(input()) for _ in range(N)]
    first_i = 0
    password = []
    for i in range(N):

        if '1' in matrix[i]:
            password = matrix[i][::-1]
            break

    first_idx = password.index('1')
    start_idx = first_idx
    check_result = []
    result = []
    for _ in range(1, 9):

        end_idx = start_idx + 7 # 시작길이 기준 7개
        check = password[start_idx:end_idx]

        for k in range(len(reversed_number)):
            if check == reversed_number[k]:
                check_result.append(k)
        start_idx = end_idx
    result = check_result[::-1]
    result_sum = 0
    odd_sum = 0
    for p in range(8):
        if p == 0 or p == 2 or p == 4 or p == 6:
            odd_sum = odd_sum + result[p]
        else:
            result_sum += result[p]
    result_sum += odd_sum*3
    if result_sum % 10 == 0:
        print(f'#{tc}', sum(result))
    else:
        print(f'#{tc}', 0)

