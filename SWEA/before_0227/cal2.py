import sys

sys.stdin = open("input/cal2.txt")

T = 10

for tc in range(1, T + 1):
    pri_dict = {"+": 2, "*": 3}
    tc_len = int(input())
    tc_str = list(input())
    result = []
    stack = []
    for i in range(tc_len):
        # 연산자
        if tc_str[i] == '*':
            while stack:
                if pri_dict[stack[-1]] < pri_dict[tc_str[i]]:
                    break
                result.append(stack.pop())
            stack.append(tc_str[i])
        elif tc_str[i] == '+':
            while stack:
                if pri_dict[stack[-1]] < pri_dict[tc_str[i]]:
                    break
                result.append(stack.pop())
            stack.append(tc_str[i])

        else:  # 피연산자
            result.append(int(tc_str[i]))

    while stack:
        result.append((stack.pop()))


    stack = []
    for j in range(tc_len):
        if result[j] == '+':
            B = stack.pop()
            A = stack.pop()
            stack.append(A + B)
        elif result[j] == '*':
            B = stack.pop()
            A = stack.pop()
            stack.append(A * B)
        else:
            stack.append(result[j])

    print("#"+str(tc),stack[-1])
