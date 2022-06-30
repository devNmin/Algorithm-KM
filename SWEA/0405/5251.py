T = int(input())

for test_case in range(1, 1 + T):

    N, E = map(int, input().split())

    # 거리, 구간 거리, 방문
    D = [float('inf')] * (N + 1)
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]

    # 그래프 생성
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w



    def get_min_index():
        min_value = 100000000
        min_index = 0
        for i in range(N + 1):
            # 방문한 적이 없는 최소 인덱스를 찾는다.
            if not visited[i] and D[i] < min_value:
                min_index = i
                min_value = D[i]
        return min_index


    def solve():
        # 0 ~ N 까지
        D[0] = 0
        visited[0] = 1
        for i in range(N + 1):

            if adj[0][i]:
                D[i] = adj[0][i]

        while 1:
            node = get_min_index()

            visited[node] = 1

            if node == N:
                return D[N]

            for x in range(N + 1):

                if adj[node][x]:

                    if D[node] + adj[node][x] < D[x]:
                        D[x] = D[node] + adj[node][x]


    print(f'#{test_case}', solve)
