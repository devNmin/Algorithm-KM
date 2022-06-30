import sys, time

sys.stdin = open('../input/5247.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [0] * 1000001

    def bfs():
        queue = [(N, 0)]

        while queue:
            current, count = queue.pop(0)

            count += 1

            for num in [current * 2, current + 1, current - 1, current - 10]:
                if 0 < num <= 1000000:

                    visited[num] = num
                    queue.append((num, count))

                    if num == M or visited[M]:
                        return count


    print(f'#{tc} {bfs()}')
