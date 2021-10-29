# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:29:10 2021

@author: Ye Jian_cheng
"""

'''DEF UTILI PER GARE '''


def SelectionSort(arr):

   for i in range(len(arr)):
      
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j                           #trova index del minimo
              
    # Swap the found minimum element with 
    # the first element        
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
   return arr





def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr
    
    

    
    
############
arr=[3,4,6,4,2,1,180,5,43,233223,544,3232,1122,444434,3,3,23,44232,23123,3,21,312,3,12,312,3,123,12,23,122,3,5,468,56,36,7,567,5,6]
arr_sorted=SelectionSort(arr)
print(arr_sorted)

