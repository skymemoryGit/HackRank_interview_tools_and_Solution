# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:20:05 2021

@author: Ye Jian_cheng
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    diz = {}

    for i in arr:
        if  not i in diz:
            diz[i] = 1   #creare la chiave i con valore 1           
        else:
            diz[i] +=1   #incrementare valore chiave

   

    key_arr=list(diz.keys())   #OTTIENI LA LISTA DELLE CHIAVI 
    ris=[]
    for i in range(0,100):
       
        if(i in key_arr):
            ris.append(diz[i])
            #print(diz[i])
        else:
            ris.append(0)
            #print(0)
        
    return ris
  
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
