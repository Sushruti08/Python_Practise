# Print a single integer that denotes the number of valleys Gary walked through during his hike.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    count = 0
    llist = []
    for i in range(n):
        if s[i]=='U':
            llist.append(1)
        else:
            llist.append(-1)
    N = 0
    for i in range(len(llist)):
        if llist[i]==1:
            if N+llist[i]==0:
               count +=1
        N +=llist[i]
    
    return count
          

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
