import sys

sys.stdin = open('input/{}.txt')


def check_e(words_list):
    result = []
    count = 0

    for word in words:
        if word == '(' or word == '{':
            result.append(word)
        elif word == ')' or word == '}':
            result.pop()

    if result:
        return 0
    else:
        return 1

T = int(input())
for test in range(1, T + 1):
    words = list(input())
    print(check_e(words))
