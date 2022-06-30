import sys

sys.stdin = open("input/cal3.txt")

T = 10

for tc in range(1, T + 1):
    isp = {"+": 1, "*": 2, "(": 0}  # in stack
    icp = {"+": 1, "*": 2, "(": 3}  # in coming
    N = int(input())
    tc_str = input()
    result = []
    stack = []
    for i in range(N):

        if tc_str[i].isdigit():
            result.append(tc_str[i])
        else:
            if len(stack) == 0:
                stack.append(tc_str[i])
            elif tc_str[i] == ')':
                while stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            elif isp[stack[-1]] < icp[tc_str[i]]:
                stack.append(tc_str[i])
            else:
                while isp[stack[-1]] >= icp[tc_str[i]]:
                    result.append(stack.pop())
                stack.append(tc_str[i])

    for j in range(len(result)):
        if result[j].isdigit():
            stack.append(result[j])
        else:
            if result[j] == '+':
                B = int(stack.pop())
                A = int(stack.pop())
                stack.append(str(A + B))
            elif result[j] == '*':
                B = int(stack.pop())
                A = int(stack.pop())
                stack.append(str(A * B))


    print("#" + str(tc), stack[-1])
