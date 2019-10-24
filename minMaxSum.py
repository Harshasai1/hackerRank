#!/bin/python3


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_array = []
    for i in arr:
        temp = arr.copy()
        temp.remove(i)
        sum_array.append(sum(temp))
    print(min(sum_array), max(sum_array))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)