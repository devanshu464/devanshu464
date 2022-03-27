#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 00:17:16 2022

@author: devanshu
"""
'''
slection sort algorithm is used to return the sortest array by
initialising i to 0, considering min_value to i, j to 1. j will 
be pointer which can keeps track of smallest element in an array for each
i. when smallest element gets by j then min_val will set set to j and swapping
the value will take place.
'''

def selection_sort(arr):
    #initialise i to 0
    i = 0
    #initialise j to 1
    j = 1
    #length of an array
    n = len(arr)
    #for each i
    
    for i in range(n):
        # for each j
        min_val = i
        for j in range(i+1,n):
            if arr[min_val] > arr[j]:
                min_val = j
                
        
        #swapping 
        arr[i],arr[min_val]= arr[min_val],arr[i]
        
        
        
    return arr
arr = [50,25,38,44,99,16,11,21]
obj = selection_sort(arr)

print(obj)