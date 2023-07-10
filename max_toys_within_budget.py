#!/bin/python3
#The first line contains two integers,  and , the number of priced toys and the amount Mark has to spend.
#The next line contains  space-separated integers 


#A toy can't be bought multiple times.

#Sample Input

#7 50
#1 12 5 111 200 1000 10
#Output
#4
#với số tiền có sẵn và giá các loại đồ chơi, mua số lượng đồ chơi max
import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    prices = sorted(prices)
    result = 0
    for i in range(len(prices)-1):
        sum = prices[i]
        j = i
        count = 1
        while sum + prices[j+1] <= k: #xét từ thằng i, cộng dồn để xem còn < k không, xong rồi đếm
            sum += prices[j+1]
            j += 1
            count += 1
            if j + 1 >= len(prices):
                break
        result = max(result, count)
    return result
            
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
