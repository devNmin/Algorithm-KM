import sys

sys.stdin = open('../input/5201.txt')

T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    # N : 컨테이너 수
    # M : 트럭 수

    product = list(map(int, input().split()))  # 화물의 무게
    truck = list(map(int, input().split()))  # 트럭 적재 용량량
    product.sort(reverse=True)
    truck.sort(reverse=True)
    # print(N, M)
    # print(product)
    # print(truck)
    result = [0 for _ in range(M)]
    for i in range(N):
        for j in range(M):
            if product[i] <= truck[j] and not result[j]:

                result[j] = (product[i])
                break
    # print(result)
    print(f"#{tc}", sum(result))
