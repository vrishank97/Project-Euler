sum1=0
for num1 in range(2,10**6):
    c=0
    for b in str(num1):
        c=c+(int(b)**5)
    if c == num1:
        sum1=sum1+num1
        print num1
print sum1
    
