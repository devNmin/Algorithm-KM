import sys

sys.stdin = open('../input/5205.txt')

T = int(input())


def my_sorted(number_list):
    if len(number_list) < 2:
        return number_list

    result = []
    p_number = number_list[0]

    down = []
    up = []

    for i in range(1, len(number_list)):
        if p_number > number_list[i]:

            down.append(number_list[i])
        else:
            up.append(number_list[i])

    down = my_sorted(down)
    up = my_sorted(up)

    result += down
    result += [p_number]
    result += up

    return result


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    print(my_sorted(numbers))
    print(f'#{tc}', my_sorted(numbers)[N // 2])
