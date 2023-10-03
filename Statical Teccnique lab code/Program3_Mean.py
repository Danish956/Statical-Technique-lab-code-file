from statistics import median
from tkinter import N


num1 = [10, 12, 54, 78, 58, 33, 24, 54, 32, 63]
n = len(num1)

print("\nData to find mean, median, mode & standard deviation:", num1)

# Calculating mean
getsum = sum(num1)
mean = getsum/n
print("Mean = ", str(mean))

# Calculating median
num1.sort()
if n % 2 == 0:
    median1 = num1[n//2]
    median2 = num1[n//2 - 1]
    median = (median1+median2)/2
else:
    median = num1[n//2]
    print("Median = " + str(median))

# Calculating mode
from collections import Counter
data = Counter(num1)
getmode = dict(data)
mode = [k for k, v in getmode.items()if v==max(list(data.values()))]
if len(mode)==n:
    getmode= "No Data Found"
else:
    getmode = "Mode = "+''.join(map(str,mode))
    print(getmode)

#Finding Standard Deviation
import numpy as np
print("Standard Deviation =", np.std(num1) )
