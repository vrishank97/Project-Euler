a=1
b=0
for a in range(1,1000):
    if a%3 == 0:
        b=a+b
    if a%5 == 0:
        b=a+b
    if a%3 == 0 and a%5 ==0:
        b=b-a
    print a
    print b
print a
print b
