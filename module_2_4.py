numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in range(2, i):
        if j != 1 and j != i and i % j == 0:
            not_primes.append(i)
            break
for i in numbers:
    if i not in not_primes and i != 1:
        primes.append(i)
print('Primes: ', primes)
print('Not_primes: ', not_primes)
