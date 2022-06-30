"""
    0210/algo_02_homework.md (1)
"""

import sys

sys.stdin = open('input/Flatten_input.txt')


# bubble sort function
def my_sorted_bubble(values):
    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]


T = 10
# 반복문 (test case)
for tc in range(1, T + 1):

    dump_count = int(input())  # dump count
    numbers = list(map(int, input().split()))

    # 0. 초기 최소 최대 값을 위한 정렬
    my_sorted_bubble(numbers)
    # 반복문 (dump count)
    for cnt in range(dump_count):
        # 1. 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없음
        if numbers[-1] - numbers[0] <= 1:
            # 1.1 출력( 주어진 덤프 횟수 이내에 평탄화가 완료 )
            print("#{}".format(tc), numbers[-1] - numbers[0])
            break
        #  2. 주어진 덤프 횟수 이내에 평탄화가 완료되지 않으면 더 이상 덤프를 수행해야 한다.
        else:
            # 2-1 최대 값-1, 최소 값 +1
            numbers[-1] -= 1
            numbers[0] += 1
            # 2-2 정렬 (정렬을 나중에 해준 이유는 dump_count만큼 반복할 때 마지막 최대 최소값 )
            my_sorted_bubble(numbers)
    # 2-3 출력 (최대 값 - 최소 값)
    else:
        print("#{}".format(tc), numbers[-1] - numbers[0])
