#!/bin/python3


# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i == 0:
            zero += 1
        else:
            neg += 1
    print(pos / len(arr))
    print(neg / len(arr))
    print(zero / len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
