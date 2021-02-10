import math
import os
import random
import re
import sys
import time

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr2 = sorted(arr)   ##  hızlı olan
    print(sum(arr2[:4]), sum(arr2[-4:]))
    #sum=0
    # for i in range(len(arr)):
    #     sum+=arr[i]
    # print ( sum-max(arr), sum-min(arr))
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    #a = float(time.time())
    miniMaxSum(arr)
    #b = float(time.time())
    #print(b - a)
