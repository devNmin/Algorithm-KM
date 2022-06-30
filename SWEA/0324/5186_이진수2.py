import sys

sys.stdin = open('../input/5186.txt')


def float_to_dec(float_num):
    result = ''
    term = 1 / 2

    cnt = 0
    while True:
        if float_num == 0:
            break
        elif cnt > 11:
            return 'overflow'

        else:
            if float_num >= term:
                float_num = float_num - term
                result += '1'
            else:
                result += '0'
            term = term / 2
            cnt += 1

    return result


T = int(input())

for tc in range(1, T + 1):
    float_number = float(input())

    print(f'#{tc}', float_to_dec(float_number))
