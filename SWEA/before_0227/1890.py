import sys

sys.stdin = open("input/1890.txt")

T = int(input())
T = 1


# 66초후 6개
def check_food(lst, M, K):
    lst.sort()
    cnt = 0
    for t in lst:
        ics = (t // M) * K
        # M초동안 기달려야 1개 이상이 나오는데 i//M 이  0이라는거는
        # 만들기전에 와버림

        if ics <= cnt:
            return 0
        else:
            cnt += 1
    return 1


for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    if check_food(numbers, M, K):
        print("#" + str(tc), "Possible")
    else:
        print("#" + str(tc), "Impossible")

    """
    예약제
    N :  먹을 자격 있는 수 74 
    M :  M초당 K개 만듬 60 60초 후 97개
    K :             97
    예시 74명 먹을수 있고 60초당 97개 만든다?
    numbers : N개 사람이 언제 도착하는지 초단위 
    
    2 2 2
    3 4
    먹을자격 2명 / 2초당 2개 / 3초 4초
    """
