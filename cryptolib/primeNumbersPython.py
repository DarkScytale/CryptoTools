import math

def isPrime(n):
    """This function test if the number n is a prime number.
    """
    maxTest = math.ceil( math.sqrt(n) + 1 )
    d = 2
    while d <= maxTest:
        if 0 == math.fmod(n, d):
            return False
        d += 1
    return True

def isPrimeOpt1(n):
    """"This function test if the number n is a prime number.
    Optimization 1: Do not test all even numbers.
    """
    if 0 == math.fmod(n, 2):
        return False
    maxTest = math.ceil( math.sqrt(n) + 1)
    d = 3
    while d <= maxTest:
        if 0 == math.fmod(n, d):
            return False
        d += 2
    return True

def isPrimeOpt2(n):
    """This function test if the number n is a prime number.
    Optimization 1: Do not test all even numbers.
    Optimization 2: Do not test all numbers ending with 5.
    """
    if 0 == math.fmod(n, 2):
        return False
    if 0 == math.fmod(n, 5):
        return False

    maxTest = math.ceil( math.sqrt(n) + 1)
    d = 3
    while d <= maxTest:
        if 5 == d & 5:
            d += 2
            continue
        if 0 == math.fmod(n, d):
            return False
        d += 2
    return True

def listPrime(n):
    """Returns a list for prime numbers included in [2, n].
    """
    l= []
    for i in range(2, n):
        if pyPrime1(n):
            l.append(i)
    return l
    
