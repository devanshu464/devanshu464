#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:30:10 2022

@author: devanshu
"""

# optimised approach of divison, without divison operator.
def divide(dividend,divisor):
    quotient = 0
    i = 0
    while dividend > divisor:
        dividend = divisor * (2 ** i)
        print(dividend)
        i = i + 1
    print("quotient",quotient)
if __name__ == '__main__':
    divide(47,4)
            