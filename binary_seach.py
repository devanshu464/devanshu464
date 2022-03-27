#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:02:25 2022

@author: devanshu
"""

def binary_search(arr,search_ele,low,high):
    if high>=low:
        mid_post = (low + high)//2
        if arr[mid_post] ==  search_ele:
            return mid_post
        elif arr[mid_post] < search_ele:
            low = mid_post + 1
            return binary_search(arr,search_ele,low,high)
        else:
            high = mid_post - 1
            return binary_search(arr,search_ele,low,high)
    else:
        return -1
    
arr = [3,4,5,6,7,8,9]
low = 0
high = len(arr) - 1
search_ele = 12
obj = binary_search(arr,search_ele,low,high)
print(obj)