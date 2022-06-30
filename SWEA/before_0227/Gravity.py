import sys

sys.stdin = open('input/Gravity_input.txt')

T = int(input())  # 3

for test in range(1, T + 1):
    test_len = int(input())  # 9 9 20
    test_list = list(map(int, input().split()))  # str->list(int)

    result = []  # 1 2 3 4 5 6  67
    for i in range(test_len - 1):  # 끝에는 안해
        cnt = 0
        for j in range(i + 1, test_len):  # j is i+1부터 끝까지
            if test_list[i] > test_list[j]:
                cnt += 1
        result.append(cnt)  # list에 cnt 저장
    print(result)

    print("#{}".format(test), max(result))  # 그중에 최대값
