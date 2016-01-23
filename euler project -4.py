largest=1
for a in range(100,999):
    for b in range(100,999):
        product=a*b
        b=b+1
        if str(product)[::-1] == str(product):
            palindrome = product
            if (palindrome>largest):
                largest=palindrome
    a=a+1
print largest
