#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
            
    pos_ratio = pos / total
    neg_ratio = neg / total
    zero_ratio = zero / total

    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)