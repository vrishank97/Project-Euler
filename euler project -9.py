a=1
b=1
c=1
for a in range(0,33):
    for b in range(0,33):
        for c in range(0,33):
            num=a**2+b**2+c**2
            if num == 1000:
                print a, b, c
            c=c+1
        b=b+1
    a=a+1
