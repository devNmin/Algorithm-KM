import sys

sys.stdin = open('input/길찾기_input.txt')

T = 1
for test in range(1, T + 1):
    tc, list_len = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(tc, list_len)
    arr1 = []
    current_p = 0
    for i in range(0, (list_len*2), 2):

        temp = [numbers[i], numbers[i + 1]]
        arr1.append(temp)

        arr1.sort()
        count = 0
        for j in range(len(arr1)):
            if arr1[j][0] == 0:
                count += 1
        for c in range(count):

            current_p = arr1[c][1]
            arr1.index()



    print(count)
    print(numbers)
    print(arr1)
    # print(tc, list_len, numbers)
