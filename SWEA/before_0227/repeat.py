import sys

sys.stdin = open("input/repeat.txt")

T = int(input())

for tc in range(1, T+1):
    arr = list(input())

    s = 0
    while s < len(arr):

        if s and arr[s] == arr[s-1]:
            del arr[s], arr[s-1]

            s -= 1
        else:
            s += 1
    print(f'#{tc} {len(arr)}')

