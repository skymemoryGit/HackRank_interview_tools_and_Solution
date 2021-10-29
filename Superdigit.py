#!/bin/python3

import math
import os
import random
import re
import sys


#ottimale 1!! 

def superDigit(n, k):
        
    # check single digits
    if k == len(n) == 1:
        return int(n)

    res = 0
    for num in n:
        res += int(num)

    return superDigit(str(res*k),1)





#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

#SOLUZIONE UN PO DEPRECATA!!!!!!  !!!!!!!!!!!!  SFRUTTATO LA VARIABILE GLOBALE


def superDigit(n, k):
    # Write your code here
        
        startinput=n*k
        print("start input", startinput)
        
        print(c)
        sumDigit(startinput)
        return c
                
        
        
        
        
       
    
    
    
    
c=0  #globale
def sumDigit(n):
    global c
    
    if (len(str(n))==1):
        c=n
        return None 
        
        
    s= str(n)
    sum=0
    for i in range(0,len(s)):
        sum=sum+int(s[i])
    #print("nel for",sum)
    
    sumDigit(sum)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
