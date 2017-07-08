import numpy
import scipy

def isPrime(n):
    """This function test with the numpy and scipy libs if n is a prime number.
    """
    maxTest = numpy.ceil( scipy.sqrt(n) + 1 )
    d = 2
    while d <= maxTest:
        if 0 == scipy.fmod(n, d):
            return False
        d += 1
    return True
    