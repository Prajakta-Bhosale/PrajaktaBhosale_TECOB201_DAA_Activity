#!/bin/python

import math
import os
import random
import re
import sys
from math import sqrt, floor, ceil

# Complete the encryption function below.
def encryption(s):
    code=s[:]
    l=len(s)
    col=int(math.ceil(l**(0.5)))
    row=int(col)-1
    if row*col<l:
        row=col
        
    l=[]
    for i in range(row):
        l.append(code[:col])
        code=code[col:]

    encrypted=''
    for i in range(col):
        for j in range(row):
            if i<len(l[j]):
                encrypted+=l[j][i]
        encrypted+=" "    

    return encrypted  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

