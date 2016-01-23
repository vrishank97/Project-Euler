sum2=0
for sum1 in range(1,101):
    sum2=sum2+sum1**2
    sum1=sum1+1
    print sum2
sum3=1
sum4=0
for sum3 in range(1,101):
    sum4=sum4+sum3
    sum3=sum3+1
sum5=sum2-(sum4**2)
print sum5
