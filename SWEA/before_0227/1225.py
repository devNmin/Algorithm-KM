import sys

sys.stdin = open("input/1225.txt")

T = 10
for _ in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    Flag = True
    while Flag:
        for i in range(1, 6):
            tmp = numbers.pop(0) - i
            if tmp <= 0:
                tmp = 0
                numbers.append(tmp)
                Flag = False
                break
            numbers.append(tmp)

    print(f"#{N}", *numbers)
