import sys
import math
import matplotlib.pyplot as plt
from scipy import stats

sys.path.append("./../")

import timeit

listNums = (
    13,
    1009,
    10007,
    100003,
    1000003,
    10000019,
    100000007,
    1000000007,
    10000000019,
    100000000003,
    1000000000039,
    100000000000031,
)
listNbSize = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15,)
listTime = list()
listLogTime = list()

nbTest = 10

for item in listNums:
    primeTime = timeit.timeit('sys.path.append("./../"); import cryptolib.primeNumbersPython as pnp; pnp.isPrime({0})'.format(item), number=nbTest)
    if 13 != item:
        listTime.append(primeTime / nbTest)
        listLogTime.append( math.log( primeTime / nbTest ) )

print("--- Régression linéaire ...")
slope, intercept, r_value, p_value, slope_std_err = stats.linregress(listNbSize, listLogTime)
listPredict = [ intercept + slope * x for x in listNbSize]
print("Equation: ")
print("Temps = Exp( {0} x NbChiffres + {0}".format(slope, intercept))

duration = math.exp( 100 * slope + intercept )
print("Temps pour un nombre de 100 chiffres : {0}".format(duration))

plt.scatter(listNbSize, listLogTime)
plt.plot(listNbSize, listPredict, 'k-')
plt.show()
print("=== FIN ===")

