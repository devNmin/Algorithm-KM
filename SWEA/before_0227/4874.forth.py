import sys

sys.stdin = open('input/4874_forth.txt')


def forth(input_list):
    stack = []

    for i in range(len(tc_str)):
        if tc_str[i] == '.':
            break
        elif tc_str[i] == '+':
            A = stack.pop()
            if stack:
                B = stack.pop()
                stack.append(A + B)
            else:
                return 'error'

        elif tc_str[i] == '*':
            A = stack.pop()
            if stack:
                B = stack.pop()
                stack.append(A * B)
            else:
                return 'error'
        else:
            stack.append(int(tc_str[i]))
    return stack[0]


T = int(input())
T = 3

for tc in range(1, T + 1):
    tc_str = input().split()

    r = forth(tc_str)
    print("#"+str(tc),r)
