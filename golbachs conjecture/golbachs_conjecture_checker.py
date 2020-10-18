# to find the two prime numbers which sum up to give the given number (accroding to golbach's conjecture) 
#  Golbachs conjecture states that any number greater than two can be written as the sum of two primes

import math

def isPrime(num):
    i = 2
    while i >= 2 and i <= int(math.sqrt(num)):
        if num % i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    num = int(input("enter the number (greater than 2) to be written as the sum of the two primes according to Golbach's conjecture: "))
    i = 2
    while i >= 2 and i <= (num/2):
        if isPrime(i) and isPrime(num-i):
            print("the required numbers are:(%d,%d)"%(i,num-i))
            break
        i += 1
