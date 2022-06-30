import sys

sys.stdin = open('input/paint_input.txt')

T = int(input())

for tc in range(1, T + 1):
    test_len = int(input())

    areas = [list(map(int, input().split())) for _ in range(test_len)]
    # 10 by 10
    total_area = [[0 for _ in range(10)] for _ in range(10)]

    for area in areas:  # 영역 하나씩 반복
        for k in range(area[0], area[2] + 1):
            for n in range(area[1], area[3] + 1):
                if area[-1] == 1:  # red
                    total_area[k][n] += 1
                else:  # blue
                    total_area[k][n] += 2
    count = 0
    for i in range(10):
        for j in range(10):
            if total_area[i][j] >= 3:  # 3 = red + blue
                count += 1

    print("#{}".format(tc), count)
