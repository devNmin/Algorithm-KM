"""
4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

N: 종점 정류장
M: 츙전기가 설치된 수 (충전기 위치)
K: 한번 충전 최대 이동 정류장 수

"""
import sys

sys.stdin = open('input/electric_bus_input.txt')

T = int(input())

# Test case 반복문
for tc in range(1, T + 1):

    K, N, M = list(map(int, input().split()))  # K N M
    M_list = list(map(int, input().split()))  # 정류장 위치
    # bus_p -> +K K-1, K-2 ... K가 0이 될때
    # K-1 K-2 K-3 ... 이사이 없으면 0 반환 

    bus_p = 0
    bus_p_cnt = 0
    station = [0 for i in range(N + 1)]  # ex) 1 0 0 1 0 1 0
    station[0] = 1
    station[-1] = 1

    for i in M_list:
        station[i] = 1

    j = K
    while True:
        if bus_p + j >= N:
            break
        else:
            if station[bus_p + j] == 1:
                bus_p = bus_p + j
                j = K
                bus_p_cnt += 1
            # -1 씩
            else:
                j -= 1
        # 충전 불가
        if j == 0:
            bus_p_cnt = 0
            break

    print(f"#{tc}", bus_p_cnt)
