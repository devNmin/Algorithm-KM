"""
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

"""
# 1,000,000
import sys
import time

from collections import deque

sys.stdin = open('../input/5247.txt')


def bfs(start, end, queue):
    # cnt = 0
    while queue:
        # print(queue)

        current, count = queue.pop(0)
        # current, count = queue.popleft()
        if current == end:
            # print(cnt)
            return count
        count += 1
        if 0 < current <= 1000000:
            # cnt += 1
            for i in range(4):
                if i == 0:
                    queue.append((current * 2, count))
                elif i == 1:
                    queue.append((current - 10, count))
                elif i == 2:
                    queue.append((current - 1, count))
                else:
                    queue.append((current + 1, count))

        # if 0 < current * 2 <= 1000000:
        #     queue.append((current * 2, count))
        # if 0 < current - 10 <= 1000000:
        #     queue.append((current - 10, count))
        # if 0 < current + 1 <= 1000000:
        #     queue.append((current + 1, count))
        # if 0 < current - 1 <= 1000000:
        #     queue.append((current - 1, count))


T = int(input())
# T = 1
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # queue = deque()

    queue = [(N, 0)]
    start_time = time.time()
    print(f'#{tc}', bfs(N, M, queue))
    end_time = time.time()
    print("WorkingTime: {} sec".format(end_time - start_time))
