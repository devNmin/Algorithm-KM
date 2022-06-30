# 1. 파스칼

import sys

sys.stdin = open('input/파스칼.txt')


# 파스칼 함수
def pascal(num):
    pa_result = [0] * num  # num 만큼 초기화
    pa_result[0] = 1  # 처음 값 1
    pa_result[-1] = 1  # 마지막 값 1

    # num이 1,2 일 때 초기화
    if num == 1:
        pa_result = [1]

    elif num == 2:
        pa_result = [1, 1]

    else:  # 1 ,2 가 아닌 다른수라면
        # 양끝 제외하고 반복문 
        for idx in range(1, num - 1):  # idx 접근방법 양끝을 제외하고 계산해주기
            pre_pa = pascal(num - 1)  # 이전 단계 파스칼 구하기
            # 이전 단계 파스칼에서 idx+idx-1하면 현재 단계 파스칼 idx 값
            pa_result[idx] = pre_pa[idx - 1] + pre_pa[idx]
    return pa_result


T = int(input())  # test case input

for tc in range(1, T + 1):  # test case만큼 반복
    number = int(input())  # 1~10 input 

    print(f"#{number}")  # 출력
    for i in range(1, number + 1):
        result = list(map(str, pascal(i)))  # 파스칼 계산
        print(' '.join(result))