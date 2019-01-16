
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 08:28:48 2019

@author: ksen
"""
import math

s = str(math.factorial(100))
sum = 0
for i in range(len(s)):
    sum = sum + int(s[i])
print (sum)
