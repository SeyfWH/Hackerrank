#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    
    for i in arr:
        if i>0:
            p=p+1
        elif i<0:
            n = n+1
        else:
            z = z +1
    
    print('%.6f'%(p/len(arr)))
    print('%.6f'%(n/len(arr)))
    print('%.6f'%(z/len(arr)))
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
