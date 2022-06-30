import sys

sys.stdin = open('input/compare_string_input.txt')

T = int(input())
for test in range(1, T + 1):
    str_1 = input()
    str_2 = input()
    result = 0
    # len(str_2) - len(str_1) +1
    for i in range(len(str_2) - len(str_1) + 1):
        if str_2[i:i + len(str_1)] == str_1:
            result = 1
            break
        else:
            result = 0

    print(f"#{test} {result}")
