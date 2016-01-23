for num in range(1,775146):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        if 600851475143%num == 0:
            largest=num
print largest
