#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 00:54:13 2022

@author: devanshu
"""
#without brute force approach
def search_2d_array(arr,search_ele):
    n = len(arr)
    i = 0
    j = n - 1
    while(i < n and j >= 0):
        if arr[i][j] == search_ele:
            return 'TRUE'
        elif arr[i][j] > search_ele:
            j = j - 1
        else:
            i = i + 1
    return 'FALSE'
        
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(arr)
obj = search_2d_array(arr,7)
print(obj)
