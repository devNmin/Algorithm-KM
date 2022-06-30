import sys

sys.stdin = open('input/paper_input.txt')


def paper(number): # 1 1 /2 3/ 3 5/ 4 11/ 5 21
    if number == 1:
        return 1
    elif number == 2:
        return 3
    else:
        return 2 * paper(number - 2) + paper(number - 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input()) // 10

    print("#"+str(tc), paper(N))
