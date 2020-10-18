# This is program to check if a given number is a prime number with run time of O(sqrt(n))

import math


def isPrime(num):
    i = 2
    while i >= 2 and i <= int(math.sqrt(num)):
        if num % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    num = int(input("Enter the number to be checked: "))
    if isPrime(num):
        print("prime")
    else:
        print("composite")
