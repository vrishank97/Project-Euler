import math
b=0
for num in range(2,2000000):
    a=0
    for num1 in range(2,int(math.sqrt(num))+1):
        if num%num1 == 0:
            a=a+1
    if a==0:
        b=b+num
print b
