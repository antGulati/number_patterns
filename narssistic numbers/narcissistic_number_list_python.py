# program to take a long integer N from the user and print all the narcissistic number between one and the given number
# narcissistic numbers are those whose sum of individual digits each raised to the power of the number of digits gives the orignal number

import math

def digitcount(num):
	return int(math.log(num,10)) + 1

def isNstc(a):
	if a <= 9 and a >= 0:
		return True
	
	q = 0
	num_digits = digitcount(a)
	
	for i in range(num_digits):
		digit = int(a/(10 ** i))
		digit = digit % 10
		q += (digit ** num_digits)
		
	if q == a:
		return True
	return False
	
if __name__ == "__main__":
    print("to find all narcissistic number between one and a given upper bound number")
    upper_bound = int(input("enter the upperbound: "))
    print("the narcissistic numbers in the given range are:")
    for i in range(1,upper_bound+1):
        if isNstc(i):
            print(i)
    
