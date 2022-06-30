'''
        2027. 대각선 출력하기

                #++++
                +#+++
                ++#++
                +++#+
                ++++#

'''

# input_str = input()
input_str = "#++++"
# print(input_str[0])
result=""
for i in range(len(input_str)):
    # print(input_str[i])
    result+=input_str[i+1]
    print(result)