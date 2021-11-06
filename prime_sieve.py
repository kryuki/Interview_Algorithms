import math

primes = []
maxVal = 1000000

isPrime = [True] * (maxVal + 1)

def genPrimes():
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, maxVal + 1):
        if isPrime[i]:
            primes.append(i)
            for j in range(i + i, maxVal + 1, i):
                isPrime[j] = False

def factorize(x):
    i = 0
    while primes[i] <= math.sqrt(x):
        if x % primes[i] == 0:
            print(primes[i], end=" ")
            x //= primes[i]
        else:
            i += 1
    if x > 1:
        print(x, end=" ")
    print()

genPrimes()
print("The first 20 primes are:")
for i in range(20):
    print(primes[i])

while True:
    x = int(input())
    factorize(x)
    if isPrime[x]:
        print(x, "is prime")
    else:
        print(x, "is not prime")
