# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:59:25 2021

@author: Ye Jian_cheng
"""

#______________________________________________________________________
#TOGLIERE RIPETIZIONI LISTA USANDO DIZ

arr = ["a", "b", "a", "c", "c", "a", "c"]
diz = {}

for i in arr:
    if  not i in diz:
        diz[i] = 1   #creare la chiave i con valore 1           
    else:
        diz[i] +=1   #increemntare valore chiave
        
print(diz)


key_arr=list(diz.keys())   #OTTIENI LA LISTA DELLE CHIAVI

for i in key_arr:          #mostra le chiavi :)
    print(i)

print(diz["a"])





    
