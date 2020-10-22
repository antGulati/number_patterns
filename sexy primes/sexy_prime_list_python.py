# program to take a long integer N from the user and print all the twin prime numbers between one and the given number
# sexy primes are those pairs of prime numbers whose difference is 6  

import math

def isPrime(num):
    i = 2
    while i >= 2 and i <= int(math.sqrt(num)):
        if num%i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    print("to find all sexy prime number between one and a given upper bound number")
    upper_bound = int(input("enter the upperbound: "))
    print("the sexy primes in the given range are:")
    for i in range(2,upper_bound+1):
        if isPrime(i) and isPrime(i+6):
            print('(%d,%d)'%(i,i+6))
