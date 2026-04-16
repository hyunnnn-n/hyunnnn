def isprime(number):
  if number == 1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

M = int(input())
N = int(input())

primes = []

for i in range(M, N + 1):
  if isprime(i):
    primes.append(i)

if not primes:
  print(-1)
else:
  print(sum(primes))
  print(min(primes))
