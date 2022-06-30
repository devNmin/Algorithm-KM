import itertools

N, M = map(int, input().split())

location = [list(map(int, input().split())) for _ in range(N)]

chicken_position = []
house_position = []

# 집, 치킨집 위치 찾기
for i in range(N):
    for j in range(N):
        if location[i][j] == 2:
            chicken_position.append((i, j))
        elif location[i][j] == 1:
            house_position.append((i, j))

combinations = list(itertools.combinations(chicken_position, M))

# combinations => 치킨집 조합

result = 1000000
for comb in combinations:
    # print("comb", comb)
    comb_sum = 0
    for house_i, house_j in house_position:
        # print("house")
        one_house = 100000  # 한집에서 가장 가까운 곳 거리
        for comb_i, comb_j in comb:  # 한집에서 전체 치킨집 다 반복해서 최소값 찾기
            # print(comb_j, comb_i)
            min_v = abs(house_i - comb_i) + abs(house_j - comb_j)

            if min_v < one_house:  # 최소값이면 업데이트
                one_house = min_v
        # print(min_sum)
        comb_sum += one_house  # 업데이트한거 적용
    if comb_sum < result:
        result = comb_sum

print(result)
