import sys

sys.stdin = open("input/2805.txt")

"""
농장의 크기는 항상 홀수
수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모
"""

T = int(input())
T = 2
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for i in range(N)]
    t = N // 2
    px, py = N // 2, N // 2
    rhombus_list = []
    sum_value = 0
    for i in range(-1 * t, (t + 1)): # -2~2
        for j in range(-1 * (t - abs(i)), t - abs(i) + 1):
            rhombus_list.append((i, j))
    print(rhombus_list)
    for dx, dy in rhombus_list:
        sum_value += matrix[px + dx][py + dy]

    print("#"+str(tc),sum_value)
