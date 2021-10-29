#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    
    ris=True
    
   
    
    mat_sorted=[]
    for i in range(0,len(grid)): 
        print(grid[i])
        elemento=grid[i]
        ls=sorted(elemento)
        mat_sorted.append(ls)
    print(mat_sorted)
    
    ls_colomn=[]
    
    for k in range(0,n-1):
        s=''
        for i in range(0,len(mat_sorted)):
            #print(mat_sorted[i][0])
            s=s+mat_sorted[i][k]+""
        #print(s)
        ls_colomn.append(s)
    
    print(ls_colomn)
    
    
    Answer="YES"
    for i in ls_colomn:
        
        ris=isInAlphabeticalOrder(i)
        if(ris==False):
            Answer=False
            return "NO"
            break
    return Answer
        
    
    
        
        
        
        
def isInAlphabeticalOrder(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True
    
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
