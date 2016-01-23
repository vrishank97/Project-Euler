total = 10000
for num1 in range(1,total):
    divisorSum1 = 0

    for div in range(1,(num1 - 1)):

        if num1%div == 0:
            divisorSum1+=div
        div+=1

    for num2 in range(1,total):
        divisorSum2=0

        for div in range(1,(num2 - 1)):

            if num1%div == 0:
                divisorSum2+=div
            div+=1
    if divisorSum1 == divisorSum2:
        amicable+=1
print amicable
        

