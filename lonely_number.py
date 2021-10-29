#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    sumP=0
    for i in range(0,n-1):
        for k in range(0,n-1):
            if(i==k):
                sumP=sumP+arr[i][k]
    
    sumS=0
    for i in range(0,n-1):
        for k in range(0,n-1):
            if(i+k==n-1):
                sumS=sumS+arr[i][k]
    
    return abs(sumP-sumS)



n=3
mat=[   [2,2,3]
            [2,3,4]
            [5,3,3]

                    ]
diagonalDifference(mat)

