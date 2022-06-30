N = 3


def selection(arr, depth):

    if sum(arr) > N-1:
        return
    if len(arr) == 2*(N-1):
        if sum(arr) == (N-1):
            #print(arr)
            #print(test)
            test.append(arr)
        return
    arr.append(0)
    selection(arr, depth+1)
    arr.pop()
    arr.append(1)
    # print(test)
    selection(arr, depth+1)

    arr.pop()
    print(test)



test = []
selection([], 0)

# print(test)