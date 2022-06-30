import sys

sys.stdin = open('../input/1242.txt')

hex_table = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
]

decode_table = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 16진수 => 2진수
    arr = [[0] * M * 4 for _ in range(N)]
    # N : 세로 줄 만큼 반복
    for i in range(N):
        hex_numbers = input()
        # M : 가로 줄 탐색 => len(hex_numbers)
        for j in range(M):
            # 16진수 => 2진수
            if hex_numbers[j].isalpha():
                number = ord(hex_numbers[j]) - ord('A') + 10
            else:
                number = int(hex_numbers[j])

            for k in range(4):
                arr[i][j * 4 + k] = hex_table[number][k]


    # arr => solve
    def solve():
        result = 0
        # 세로
        for i in range(N):
            # 가로
            j = M * 4 - 1
            while 0 < j:
                if arr[i][j] == 1 and arr[i - 1][j] == 0:
                    # 숫자 8개 만큼 조사
                    code = [0] * 8
                    for k in range(7, -1, -1):
                        x = 0
                        y = 0
                        z = 0
                        while arr[i][j] == 1:
                            # 보고있는 정보 1이면 반복
                            z += 1  # 4번째의 1의 갯수
                            j -= 1

                        while arr[i][j] == 0:
                            y += 1  # 3번째의 0의 갯수
                            j -= 1

                        while arr[i][j] == 1:
                            x += 1  # 2번째의 1의 갯수
                            j -= 1

                        while arr[i][j] == 0:
                            j -= 1
                        # 1줄 검사가 끝!
                        d = min(x, y, z)
                        x //= d
                        y //= d
                        z //= d
                        code[k] = decode_table.get((x, y, z))
                    # 숫자 8개 준비
                    sum_value = 0
                    for t in range(8):
                        if t % 2:
                            #
                            sum_value += code[t]
                        else:
                            sum_value += code[t] * 3
                    if sum_value % 10 == 0:
                        result += sum(code)
                    j += 1
                j -= 1

        return result


    print(f'#{tc} {solve()}')


"""
############## 교수님 코드 ###########################
hex_table = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
]

decode_table = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [[0] * M * 4 for _ in range(N)]
    # N : 세로 줄 만큼 반복
    for i in range(N):
        hex_numbers = input()
        # M : 가로 줄 탐색 => len(hex_numbers)
        for j in range(M):
            # 16진수 => 2진수
            if hex_numbers[j].isalpha():
                number = ord(hex_numbers[j]) - ord('A') + 10
            else:
                number = int(hex_numbers[j])

            for k in range(4):
                arr[i][j * 4 + k] = hex_table[number][k]


    def solve():
        result = 0
        # 세로
        for i in range(N):
            # 가로
            j = M * 4 - 1
            while 0 < j:
                if arr[i][j] == 1 and arr[i - 1][j] == 0:
                    # 숫자 8개 만큼 조사
                    code = [0] * 8
                    for k in range(7, -1, -1):
                        x = 0
                        y = 0
                        z = 0
                        while arr[i][j] == 1:
                            # 보고 있는 정보가 1이면 반복
                            z += 1  # 4번째의 1의 갯수
                            j -= 1
                        while arr[i][j] == 0:
                            y += 1  # 3번쨰의 0의 갯수
                            j -= 1
                        while arr[i][j] == 1:
                            x += 1  # 2번째의 1의 갯수
                            j -= 1
                        while arr[i][j] == 0:
                            j -= 1
                        # 1줄 검사가 끝 => 비율 구성
                        d = min(x, y, z)
                        x //= d
                        y //= d
                        z //= d
                        code[k] = decode_table.get((x, y, z))
                    # 숫자 8개 준비
                    sum_value = 0
                    for t in range(8):
                        if t % 2:
                            sum_value += code[t]
                        else:
                            sum_value += code[t] * 3
                    if sum_value % 10 == 0:
                        result += sum(code)
                    j += 1
                j -= 1
        return result


    print(f'#{tc} {solve()}')
"""