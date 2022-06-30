import sys

sys.stdin = open('input/binary_search_input.txt')

T = int(input())
T = 3
for tc in range(1, T + 1):
    P, Pa, Pb = list(map(int, input().split()))
    c_A = 0
    l_A = 1
    r_A = P
    c_B = 0
    l_B = 1
    r_B = P
    cnt_A = 0
    cnt_B = 0
    while True:

        c_A = int((l_A + r_A) / 2)
        c_B = int((l_B + r_B) / 2)

        if c_A != Pa:
            cnt_A += 1
            if c_A < Pa:
                l_A = c_A
            else:
                r_A = c_A
        if c_B != Pb:
            cnt_B += 1
            if c_B < Pb:
                l_B = c_B
            else:
                r_B = c_B

        if c_A == Pa or c_B == Pb:
            # print(cnt_A, cnt_B)
            if cnt_A > cnt_B:
                print(f"{tc} B")
            elif cnt_A < cnt_B:
                print(f"{tc} A")
            else:
                print(f"{tc} 0")
            break


