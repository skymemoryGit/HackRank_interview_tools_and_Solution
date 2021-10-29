# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    X= findmin(arr)
    Y=findmax(arr)
    
    minsum=0
    
    
    
                
    if(arr[0]==arr[1]==arr[2]==arr[3]==arr[4]):
        print(str(arr[0]*4)+" "+str(arr[0]*4))
    
    else:
    
        
            
        for i in range(0,len(arr)):
            passato=False
            if(arr[i]!=Y ):    #esclude max
                minsum=minsum+arr[i]
        
        maxsum=0
        for i in range(0,len(arr)):
            if(arr[i]!=X):    #esclude min
                maxsum=maxsum+arr[i]
                
        print(str(minsum)+" "+str(maxsum))
    
    
    
    

def findmin(arr):
    min=arr[0]
    for i in range(0,len(arr)):
        if(arr[i]<min):
            min=arr[i]
    return min
        
    
def findmax(arr):
    max=arr[0]
    for i in range(0,len(arr)):
        if(arr[i]>max):
            max=arr[i]
    return max
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
