'''
    2070. 큰 놈, 작은 놈, 같은 놈

[제약 사항]

각 수는 0 이상 10000 이하의 정수이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.

'''
T = int(input()) #입력 개수 

for test_case in range(1, T + 1):
    #3 5
    result = list(map(int,input().split())) # result[0] result[1] 비교
    
    if result[0] > result[1]:

        print("#{} >".format(test_case))

    elif result[0] == result[1]:

        print("#{} =".format(test_case))

    else:
        print("#{} <".format(test_case))
    