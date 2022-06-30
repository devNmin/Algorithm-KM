import sys

sys.stdin = open('../input/5185.txt')


def hex_to_dec(hex_num):
    hex_list = ['A', 'B', 'C', 'D', 'E', 'F']
    if hex_num == 'A':
        number = 10
    elif hex_num == 'B':
        number = 11
    elif hex_num == 'C':
        number = 12
    elif hex_num == 'D':
        number = 13
    elif hex_num == 'E':
        number = 14
    elif hex_num == 'F':
        number = 15
    else:
        number = int(hex_num)

    num_list = ['0', '0', '0', '0']  # 4자리씩 나누기 위해

    idx = -1  # 뒤에서 부터 하나씩 앞으로 가기 위해

    while True:
        s, r = divmod(number, 2)  # s 몫 r 나머지
        number = number // 2
        num_list[idx] = str(r)

        if s == 0 or s == 1:
            idx -= 1
            num_list[idx] = str(s)  # 마지막 값
            break

        idx -= 1

    return num_list


T = int(input())

for tc in range(1, T + 1):
    _, Hex = map(str, input().split())

    dec_list = []
    for h in Hex:  # 전체 리스트로 만들어준다 4개씩 끊은 리스트를
        dec_list += hex_to_dec(h)

    result = ''
    for d in dec_list:  # 리스트 값 하나씩
        result += d

    print(f'#{tc}', result)
