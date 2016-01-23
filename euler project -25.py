sum1=0
sum2=1
sum3=0
sum4=0
counter = 0
while counter in range (0,10000):
    sum3=sum1+sum2
    sum1=sum2
    sum2=sum3
    counter=counter+1
    if len(str(sum3))==1000:
        break
print sum3,counter+1
