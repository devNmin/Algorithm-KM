# list1 = [7, 5, 9, 3, 6]
# list2 = [7, 5, 5, 5, 8]

list1 = [9, 9 ,9, 2 ]
list2 = [6,6,6,6,6]


l1_sum = 0
l2_sum = 0
total_list = []
for l1 in list1:
    l1_sum += l1 ** 2
for l2 in list2:
    l2_sum += l2 ** 2

print(sum(list1), sum(list2))

print(l1_sum , l2_sum)
print("fuckkkkkkkkkkkkkkkkk",l1_sum + l2_sum)

"""
j = 0
        while j < N:

            j_sum = 0
            if j < N - M + 1:
                for c in range(M):  # 벌통수만큼 반복
                    # print('a', j_sum)
                    j_sum += mat[i][j + c]
                    # print('b', j_sum)
                if j_sum == C:
                    for c in range(M):
                        result.append(mat[i][j + c])
            j += 1
            print(i, j, j_sum)
1 2 13
1 3 13
1 4 0
2 1 7
2 2 9
2 3 8
2 4 0
3 1 10
3 2 8
3 3 13
3 4 0
[8, 5, 5, 8, 6, 7]
[89, 89, 85]

0 0 7
0 1 10
0 2 16
0 3 0
1 0 17
1 1 13
1 2 13
1 3 0
2 0 7
2 1 9
2 2 8
2 3 0
3 0 10
3 1 8
3 2 13
3 3 0
[8, 5, 5, 8, 6, 7]
[89, 89, 85]
"""