#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 01:52:04 2022

@author: devanshu
"""

# Merge sort implementation
def merge_sort(arr):
    
    if len(arr) > 1:
        #mid of an array
        mid = len(arr)//2
        #left subarray
        L = arr[:mid]
        #right subarray
        R = arr[mid:]
        #recursive call to merge_sort for left and right subaaray
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j + 1
            k = k +1
        #checking if any element was left 
        while i < len(L):
            arr[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1
def print_sorted_array(arr):
    for i in range(len(arr)):
        print(arr[i],end= " ")
    print()
        #print("sorted arra",arr)
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("given array",arr)
    merge_sort(arr)
    print_sorted_array(arr)
    
    
        
            
                