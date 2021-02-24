import math
import os
import random
import re
import sys



n = int(input("n: "))

c = list(map(int, input().rstrip().split()))

jmp = 0

skip = False

for i in range(1, len(c)):
    if c[i] == 0:
        jmp += 1
        if 1 <= i < len(c)-1:
            if c[i+1] == 0:
                if c[i-1] == 0:
                    if skip is False:
                        jmp -= 1
                        skip = True
                    else:
                        skip = False
    else:
        skip = False



print(jmp)

