x=23
count=0
import math
while x <=100:
    for y in range(0,x):
        z= math.factorial(x)/(math.factorial(y)*math.factorial(x-y))
        if z>1000000:
            count+=1
    x+=1
print count
