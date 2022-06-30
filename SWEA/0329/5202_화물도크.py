import sys

sys.stdin = open('../input/5202.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dock = [list(map(int, input().split())) for _ in range(N)]
    # 끝나는 시간을 기준으로 정렬
    dock.sort(key=lambda x: x[1])

    cnt = 1
    end = dock.pop(0)  # 맨 처음꺼 뽑음

    # 다음 시작이 앞의 끝나는 시간안에 있으면 삭제
    while dock:

        if dock[0][0] < end[1]:
            dock.pop(0)

        else:
            cnt += 1
            end = dock.pop(0)  # 갱신

    print("#{} {}".format(tc, cnt))