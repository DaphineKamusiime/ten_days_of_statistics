#https://www.hackerrank.com/challenges/s10-basic-statistics


from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

# Calculate mean
mean = sum(arr) / n
print(round(mean, 1))

# Calculate median
arr.sort()
if n % 2 == 0:
    median = (arr[n//2 - 1] + arr[n//2]) / 2
else:
    median = arr[n//2]
print(round(median, 1))

# Calculate mode
counts = Counter(arr)
mode = max(counts, key=counts.get)
print(mode)


#https://www.hackerrank.com/challenges/s10-weighted-mean/
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    
    weighted_sum = 0
    weight_sum = 0

    for i in range(len(X)):
        weighted_sum += X[i] * W[i]
        weight_sum += W[i]

    weighted_mean = weighted_sum / weight_sum
    print("{:.1f}".format(weighted_mean))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
