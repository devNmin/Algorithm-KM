import sys

sys.stdin = open('../input/1231.txt')

def inorder(n):
    global word
    if n <= N:
        inorder(n * 2)
        word += lists[n - 1][1]
        inorder(n * 2 + 1)


T = 10
for tc in range(1, 1 + T):
    word = ''
    N = int(input())
    lists = [list(input().split()) for _ in range(N)]

    inorder(1)
    print(f"#{tc}", word)
