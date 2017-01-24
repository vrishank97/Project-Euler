x=1
y=0
z=2
a=0
while x <=1002001:
    y=y+1
    print x
    a=a+x
    x=x+z
    if y%4 == 0:
        z=z+2
print a
