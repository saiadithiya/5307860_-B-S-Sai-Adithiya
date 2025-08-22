#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    from collections import Counter
    freq = Counter(s)
    counts = list(freq.values())
    freq_count = Counter(counts)

    if len(freq_count) == 1:
        return "YES"
    elif len(freq_count) == 2:
        key1, key2 = freq_count.keys()
        if (freq_count[key1] == 1 and (key1 - 1 == key2 or key1 - 1 == 0)) or (freq_count[key2] == 1 and (key2 - 1 == key1 or key2 - 1 == 0)):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()