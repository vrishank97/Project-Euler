a=0
for num in range(1,100000):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        a=a+1
        if (a == 10002):
            break
print num
