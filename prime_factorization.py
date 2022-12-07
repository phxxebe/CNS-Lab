# 2020BTECS00201 Vaishnavi Pawar

import math
import time

def primeFactors(n):
    arr = []
    # print the number of 2s that divide n
    while n % 2 == 0:
        arr.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            arr.append(i)
            n = n / i

    # condition if n is a prime number greater than 2
    if n > 2:
        arr.append(n)
    return arr

semiprimes = [100000000088787877679, 10000000000097987989, 1000000000099987889, 100000005178888819, 10000000058888887, 1000000518888883, 100000008888889, 10000079888899, 1000010666663]
digit = [21, 20, 19, 18, 17, 16, 15, 14, 13]

for i in range(len(semiprimes)-1, -1, -1):

    start = time.time()
    l = primeFactors(semiprimes[i])
    end = time.time()

    print("Prime Factors: ", l)
    print("Semiprime: ", semiprimes[i])
    print("Number of Digits: ", digit[i])
    print("Time Elapsed: ", end - start)
    print()