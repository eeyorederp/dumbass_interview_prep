#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valleys = 0
    level = 0
    for i in range(len(path)):
        if path[i] == "D":
            level -= 1
        elif path[i] == "U":
            level += 1
            if level == 0:
                valleys += 1
    return valleys
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(raw_input().strip())

    path = raw_input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()