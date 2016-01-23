x=100
y=0
for a in range(1,x):
    for b in range(1,x):
        for c in range(1,x):
            if a**2+b**2==c**2:
                y=y+1
print y
