import sys

sys.stdin = open('../input/5204.txt')


def my_sort(in_list):
    global cnt

    if len(in_list) == 1:
        return in_list

    n = len(in_list)
    l1 = in_list[0:n // 2]
    l2 = in_list[n // 2:n]
    my_sort(l1)
    my_sort(l2)

    idx = l_idx = r_idx = 0

    while l_idx < len(l1) and r_idx < len(l2):
        if l1[l_idx] <= l2[r_idx]:
            in_list[idx] = l1[l_idx]
            l_idx += 1
        else:
            in_list[idx] = l2[r_idx]
            r_idx += 1
        idx += 1
    if l_idx == len(l1):

        for i in range(r_idx, len(l2)):
            in_list[idx] = l2[i]
            idx += 1

    elif r_idx == len(l2):
        cnt += 1
        for i in range(l_idx, len(l1)):
            in_list[idx] = l1[i]
            idx += 1
    return in_list


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    result = my_sort(numbers)

    print(f'#{tc}', result[N//2], cnt)
