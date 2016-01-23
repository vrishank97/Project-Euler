sum1=1
sum2=1
sum3=0
sum4=0
while sum3 in range (0,4000000):
    sum3=sum1+sum2
    sum1=sum2
    sum2=sum3
    print sum3-sum1
    if sum3%2 == 0:
        sum4=sum4+sum3
print sum4
    
