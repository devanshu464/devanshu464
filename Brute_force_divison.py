#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:13:48 2022

@author: devanshu
"""

# Divison without using divison operator
# applying brute force approach
def divide(dividend,divisor):   
    quotient = 0
    if dividend > 0 and divisor >0:
        # excute the code while dividend is less than divisor and increase
        # quotient by 1 in each execution
        while dividend >= divisor:
            dividend = dividend - divisor
            quotient += 1
        print("quotient", quotient)
    else:
        print("check the value of dividend and divisor! both must > 0")
if __name__ == '__main__':
   divide(5555555,3)
    
        