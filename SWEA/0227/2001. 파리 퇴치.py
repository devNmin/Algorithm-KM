import sys

sys.stdin = open("../input/2001.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0

    # sum_lists = [(0, 0), (1,0) ,(0,1), (1,1)]
    sum_lists = []

    for x in range(M):
        for y in range(M):
            sum_lists.append((x, y))

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_value = 0
            for dx, dy in sum_lists:
                sum_value += matrix[i+dx][j+dy]

            if max_value < sum_value:
                max_value = sum_value
    print(f"#{tc}", max_value)

"""
N 은 5 이상 15 이하이다.

2. M은 2 이상 N 이하이다.

3. 각 영역의 파리 갯수는 30 이하 이다.

"""
