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

def listPrime(n):
    """Returns a list for prime numbers included in [2, n].
    """
    l= []
    for i in range(2, n):
        if pyPrime1(n):
            l.append(i)
    return l
    