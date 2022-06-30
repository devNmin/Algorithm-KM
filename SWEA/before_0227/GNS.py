import sys

sys.stdin = open('input/GNS_test_input.txt')

T = int(input())

numbers_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
                'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9,
                0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR',
                5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'
                }

for test in range(1, T + 1):

    test_len = list(map(str, input().split())) # #1 7041
    test_list = list(map(str, input().split()))
    result_str = ''
    result_list = []

    for i in range(int(test_len[1])):
        result_list.append(numbers_dict[test_list[i]])

    result_list.sort()

    for i in result_list:
        result_str += numbers_dict[i] + ' '

    print(f"#{test}")
    print(result_str)
