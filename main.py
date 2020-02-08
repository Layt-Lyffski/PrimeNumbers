

def isPrime (n):
  if n < 1:
    return False
  for i in range (2, n, 1): #initial value, till n reached, in 1 steps //"like" for loop
    if n % i == 0:
      return False
  return True

def sieve (n):
  primes = []
  numbers = list(range(2, n))
  i = 2
  while i * i < n:
    for k in range(i, n, i):
      if k in numbers:
        numbers.remove(k)
    primes.append(i)
    i = numbers [0]
  return primes + numbers

def Fermattest(p):
  from random import randrange
  return randrange(2, p) ** (p-1) % p == 1

print(isPrime(13))
print(sieve(100))
print(Fermattest(13))

