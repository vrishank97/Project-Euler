num1=0
num2=1
while num4 in range(0,5):
    num1=num1+num2
    num2=num2+1
    num4=0
    for num3 in range(1,50):
        if num1%num3 == 0:
            num4=num4+1
            print num4
        num3=num3+1
print num1
        
