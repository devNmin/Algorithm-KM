

'''

    1545. 거꾸로 출력해 보아요

주어진 숫자부터 0까지 순서대로 찍어보세요

아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다

'''

T = input()
numbers = int(T)
result = ''
for i in range(numbers+1):

    result = str(i)+' '+result

print(result)