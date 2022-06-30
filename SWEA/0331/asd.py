import sys

sys.stdin = open('../input/5205.txt')

T = int(input())


def quick(data):
    # 재귀 함수 종료 조건
    if len(data) < 2:
        return data

    result = []
    # pivot값 설정
    pivot = data[0]

    # pivot보다 작거나 큰 값 리스트
    low = []
    high = []

    # pivot보다 작으면 low, 크면 high에 저장
    for i in range(1, len(data)):
        if pivot > data[i]:
            low.append(data[i])
        else:
            high.append(data[i])

    # 결과값 low, high 리스트에 대해 각각 quick정렬
    low = quick(low)
    high = quick(high)

    # 정렬된 값들을 하나로 병합
    result += low
    result += [pivot]
    result += high

    return result


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    print(quick(numbers))
    print(f'#{tc}', quick(numbers)[N // 2])
