import sys

# sys.stdin = open('../input/1242_2.txt')
sys.stdin = open('../input/1242_2.txt')


# hex to dec
def hex_to_dec(hex_num):
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

    num_list = ['0', '0', '0', '0']
    s = 0

    idx = -1
    while True:
        s, r = divmod(number, 2)
        number = number // 2
        num_list[idx] = str(r)

        if s == 0 or s == 1:
            idx -= 1
            num_list[idx] = str(s)
            break
        idx -= 1

    return num_list


# ratio password 0 1 0 1
def change_password(password_list, ratio):
    reversed_number = [
        [3, 2, 1, 1],
        [2, 2, 2, 1],
        [2, 1, 2, 2],
        [1, 4, 1, 1],
        [1, 1, 3, 2],
        [1, 2, 3, 1],
        [1, 1, 1, 4],
        [1, 3, 1, 2],
        [1, 2, 1, 3],
        [3, 1, 1, 2],
    ]
    check_list = [0, 0, 0, 0]
    idx = -1
    flag = '1'
    print(password_list)

    for z in range(len(password_list)):  # 7 ?

        if idx == -4:
            check_list[idx] += 1
            if z == len(password_list) - 1:
                break
        else:
            if password_list[(z + 1) * -1] == flag:
                check_list[idx] += 1
            if password_list[(z + 1) * -1] != password_list[((z + 1) * -1) - 1]:  # 앞뒤가 다르면
                idx -= 1
                if flag == '1':
                    flag = '0'
                elif flag == '0':
                    flag = '1'

    for c in range(len(check_list)):
        check_list[c] = int(check_list[c] / ratio)

    for i in range(len(reversed_number)):
        if reversed_number[i] == check_list:
            # print(i, "찾음")
            return i


#############################
T = int(input())
T = 1
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [list(input()) for _ in range(N)]
    break_flag = 0
    password = []
    if N <= 100:
        for i in range(N):
            for j in range(M):
                if matrix[i][j] != '0':
                    password = matrix[i]
                    break_flag = 1
                    break
            if break_flag:
                break

    dec_list = []
    result = ''
    si = 0
    fi = 0
    print("passw", password)
    for ccc in range(len(password)):
        if password[ccc] != '0':
            si = ccc
            break
    for ccf in range(len(password)):
        if password[::-1][ccf] != '0':
            fi = ccf
            break
    print(si, len(password) - fi, password)
    for i in range(si, len(password) - fi):  # 8 ~22
        dec_list += hex_to_dec(password[i])

    for d in dec_list:
        result += d
    print(result)

    start_idx = 0

    result_list = list(result)[::-1]
    fii = 0
    for fidx in range(len(result_list)):
        if result_list[fidx] != '0':
            fii = fidx
            break
    print('asd', len(result_list)-fii)
    # len(result_list)-fii-1 마지막 idx
    print(result[len(result_list)-fii-1])

    # print(result[::-1])
    # print(result_list)
    for c in range(len(result_list)):

        if result_list[c] == '1':
            start_idx = c
            break
    # print(start_idx)

    b = ''
    print(start_idx)
    for i in range(start_idx, start_idx + 57, 7):
        b += str(change_password(result[i:i + 7], 1))

    # print(b)
    b = list(b)
    # print(b)
    result_sum = 0
    odd_sum = 0
    for p in range(8):
        if p == 0 or p == 2 or p == 4 or p == 6:
            odd_sum = odd_sum + int(b[p])
        else:
            result_sum += int(b[p])
    result_sum += odd_sum * 3
    b = map(int, b)
    if result_sum % 10 == 0:
        print(f'#{tc}', sum(b))
    else:
        print(f'#{tc}', 0)
