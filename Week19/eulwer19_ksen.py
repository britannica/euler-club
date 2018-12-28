#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:30:43 2018

@author: ksen
"""
# Euler 19

month = [31,28,31,30,31,30,31,31,30,31,30,31]
days = 0
sundays = 0
for y in range(1900,2001):
    for m in range(0,12):
        if ((days % 7 == 0) & (y > 1900)):
            sundays = sundays + 1
        days = days + month[m] + leap(y,m)
print (sundays)


def leap(y,m):
    if (m != 1):
        return 0
    else:
        if((y % 4 == 0) & (y % 400 != 0)):
            return 1
        else:
            return 0
