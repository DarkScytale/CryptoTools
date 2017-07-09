from cryptolib import primeNumbersPython as pnp
from cryptolib import primeNumbersNumSci as pnns

import timeit

nbTest = 10
numberToTest = 100000000000031

print("Lancement du test de vitesse des fonctions en pure Python ...")

tPython1 = timeit.timeit('import cryptolib.primeNumbersPython as pnp; pnp.isPrime({0})'.format(numberToTest), number=nbTest)

print("Fonction de base : {0}".format(tPython1))

print("FIN")

