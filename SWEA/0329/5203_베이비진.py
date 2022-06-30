import sys

sys.stdin = open('../input/5203.txt')

T = int(input())


for tc in range(1, 1 + T):
    lists = list(map(int, input().split()))

    l1 = []
    l1_check = [0] * 10
    l2 = []
    l2_check = [0] * 10
    result = 0
    for i in range(0, 12, 2):

        l1.append(lists[i])
        l1_check[lists[i]] += 1
        if l1_check[lists[i]] == 3:  # triplet 체크
            result = 1
            break
        l2.append(lists[i + 1])
        l2_check[lists[i + 1]] += 1
        if l2_check[lists[i]] == 3:  # triplet 체크
            result = 2
            break

        for k in range(len(l1_check) - 2):
            if 1 <= l1_check[k] and 1 <= l1_check[k + 1] and 1 <= l1_check[k + 2]:
                result = 1
                break
            elif 1 <= l2_check[k] and 1 <= l2_check[k + 1] and 1 <= l2_check[k + 2]:
                result = 2
                break
            else:
                result = 0

    print(f'#{tc}', result)
