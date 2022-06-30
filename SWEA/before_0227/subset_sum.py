import sys

sys.stdin = open('input/subset_input.txt')

T = int(input())
T =1
for tc in range(1, T + 1):
    # 1~12 숫자의 집합
    # N : 부분 집합의 원소의 수
    # K : 부분 집합의 합
    N, K = list(map(int, input().split()))
    my_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # my_set = [1, 2, 3, 4, 5]
    n = len(my_set)
    count = 0
    for i in range(1 << n): # 2^12-1
        sum = 0
        for j in range(n): # 0 ~ 11
            if i & (1 << j):

                sum += my_set[j]
                if sum == K:
                    count += 1
                print(my_set[j],end=", ")
                print("sum:",sum, end=", ")
        print()
    print()
    print(count)
