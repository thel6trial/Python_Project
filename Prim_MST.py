#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#
# nhập vào mảng 3 chiều gồm: đỉnh 1 - đỉnh 2 - khoảng cách 2 đỉnh
def prims(n, edges, start): #start là đỉnh bắt đầu
    # Write your code here
    prim = {start} #nạp vào prim
    sum = 0
    while(len(prim) < n):
        new_edges = [e for e in edges if ((e[0] not in prim and e[1] in prim) or (e[0] in prim and e[1] not in prim))]
        #new_edges là tập các cạnh kề với các cạnh đã có trong prim
        b = min(new_edges, key = lambda e:e[2]) #lấy max khoảng cách
        prim.update(b[:2]) #update vào prim
        sum += b[2] #update tổng trọng số
    return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
