import math
import pandas as pd
file = open("advCodePuzzleDay3part1.txt")
Sum=0
adv=[]
for row in file:

    adv.append(row)

for line in adv:
    b1=[]
    a1=[]
    b=0
    b=(len(line))/2
    
    for i in range (0, b):
        a1.append(ord(line[i]))

    for k in range(len(a1)):
        if a1[k] >=97:
            a1[k] = a1[k] - 96
        elif a1[k] < 97:
            a1[k] = a1[k] - 38

    for j in range(b,len(line)):
        b1.append(ord(line[j]))

    for m in range(len(b1)):
        if b1[m] >=97:
            b1[m] = b1[m] - 96
        elif b1[m] < 97:
            b1[m] = b1[m] - 38

    result = 0
    for a1Val in a1:
        for b1Val in b1:
            if a1Val==b1Val:
                result= a1Val
                break
         

    Sum = Sum+result               
print(Sum)
