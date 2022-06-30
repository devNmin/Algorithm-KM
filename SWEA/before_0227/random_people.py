import random


def draw_problem(people_list, problems):
    # 셔플
    random.shuffle(people_list)
    print("*" * 37)
    for problem in problems:
        # 랜덤한 번호
        random_number = random.randint(0, len(people_list) - 1)
        # 결과 출력
        print(f"* {people_list[random_number]}님 {problem} 문제 당첨을 축하 드립니다. *")
        # 뽑히면 제거
        people_list.pop(random_number)
    print("*" * 37)

# people_all = ['권혁림', '김보연', '김은혜', '김진하', '김찬일', '김호진', '박호현', '배건길', '유강현', '윤영훈', '이선주', '이슬기', '장종훈', '전상현', '전희성', '정인용', '조경민', '조성규', '조성환', '조유진', '진윤아', '천소희']
people = ['경민', '인용', '진하', '소희', '희성']
problem_numbers = ['1','2','3']

draw_problem(people, problem_numbers)