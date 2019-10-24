#!/bin/python3

import os

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    split_list = s.split(':')
    if split_list[-1][-2:] == "PM" and int(split_list[0]) < 12:
        split_list[0] = int(split_list[0])
        split_list[0] = 12 + split_list[0]
    
    
    elif split_list[-1][-2:] == "AM" and int(split_list[0]) == 12:
        split_list[0] = '00'
    split_list[-1] = split_list[-1].strip(split_list[-1][-2:])
    return ":".join(list(map(str, split_list)))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
