#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = []
    k = k % 26 
    
    for char in s:
        if char.isalpha():
            if char.isupper():
                shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            else:
                shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        else:
            result.append(char) 
    
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
