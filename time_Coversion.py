#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if(s[8]=='P'): #check if pm or am 
       
    
        hh=int(s[0]+s[1])
        if(hh==12):
            hh=str(12)
        else:
            hh=str(hh+12)
        
        
        
        
        
        
        
        mm=s[3]+s[4]
        ss=s[6]+s[7]
        print(hh+":"+mm+":"+ss)
        return hh+":"+mm+":"+ss
    
    if(s[8]=='A'): #check if pm or am 
        hh=int(s[0]+s[1]) 
        
        hh_str=str(hh%12)
        if(len(hh_str)==1):
            hh_str="0"+hh_str
        
        
        mm=s[3]+s[4]
        ss=s[6]+s[7]
        
        
        
        print(hh_str+":"+mm+":"+ss)
        
        
        return str(hh_str)+":"+mm+":"+ss
    
        
        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
