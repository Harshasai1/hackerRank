#!/bin/python3

import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique_elements, pairs_count = list(set(ar)), 0
    for item in unique_elements:
        temp_var = ar.count(item)
        pairs_count += temp_var // 2
    return pairs_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
