#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) %2 != 0:
        return -1
    a = [*s[:len(s)//2]]
    b = [*s[len(s)//2:]]
    c = 0
    for i in a:
        if i not in b:
            c += 1
        else:
            b.remove(i)          
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
