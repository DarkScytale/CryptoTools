import sys, os, importlib

#from cryptolib import primeNumbersPython as pnp
#from cryptolib import primeNumbersNumSci as pnns

import timeit

nbTest = 10

numberToTest = 100000000000031

print("Lancement du test de vitesse des fonctions en pure Python ...")

tPython1 = timeit.timeit('sys.path.append("./../"); import cryptolib.primeNumbersPython as pnp; pnp.isPrime({0})'.format(numberToTest), number=nbTest)
print("Fonction de base : {0} sec".format(tPython1/nbTest))

tPython2 = timeit.timeit('sys.path.append("./../"); import cryptolib.primeNumbersPython as pnp; pnp.isPrimeOpt1({0})'.format(numberToTest), number=nbTest)
print("Fonction optimise 1 : {0} sec".format(tPython2/nbTest))

tPython3 = timeit.timeit('sys.path.append("./../"); import cryptolib.primeNumbersPython as pnp; pnp.isPrimeOpt2({0})'.format(numberToTest), number=nbTest)
print("Fonction optimise 2 : {0} sec".format(tPython3/nbTest))

print("FIN")

