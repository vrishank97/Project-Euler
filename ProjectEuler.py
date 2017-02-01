#reverses a given integer
def reverse(n):
	rev=0
	while(n!=0):
		rev=rev*10+n%10
		n/=10
	return rev

#Primality test
def isPrime(n):
	if(n<=1):
		return False
	if n%2==0:
		return False
	if n==2:
		return True
	for i in xrange(3, int(n**0.5+1)):
		if(n%i==0):
			return False
	return True

#counts the digits in an integer
def countDigits(n):
	count=0
	while(n!=0):
		count+=1
		n/=10
	return count

#returns the prime factors of a number
def primeFactors(n):
	factors=[]
	for i in range(2, n**0.5+1):
		if n%i==0 and isPrime(i):
			factors.append(i)
	return factors

#returns the digits of the number
def digits(n):
	digits=[]
	while(n!=0):
		digits.append(n%10)
		n/=10
	return digits