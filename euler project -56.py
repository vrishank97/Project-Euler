maximum = 0
for a in range(90,100):
    for b in range(90,100):
        x=0
        for c in str(a**b):
            x=x+int(c)
            if x > maximum:
                maximum=x
print maximum
