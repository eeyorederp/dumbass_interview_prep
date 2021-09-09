#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    wordDict = {}
    for word in magazine:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    for word in note:
        if word not in wordDict:
            print "No"
            return
        else:
            wordDict[word] -= 1
            if wordDict[word] < 0:
                print "No"
                return
    print "Yes"

if __name__ == '__main__':
    first_multiple_input = raw_input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
