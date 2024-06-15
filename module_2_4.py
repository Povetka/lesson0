numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in range(2, i + 1):
        if j != 1 and j != i and i % j == 0:
            if i not in not_primes:
                not_primes.append(i)
            if i in not_primes:
                pass
        else:
            if i in not_primes:
                pass
            if i not in primes:
                primes.append(i)
            if i in primes:
                pass
print('primes: ', primes)
print('not_primes: ', not_primes)


# for i in numbers:
#     for j in range(1, i + 1):
#         if j != 1 and j != i and i % j == 0:
#             if i not in not_primes:
#                 not_primes.append(i)
#             if i in not_primes:
#                 pass
#         if i % 1 == 0 and i % i == 0 and i != 1:
#             if i not in primes:
#                 primes.append(i)
#             if i in primes:
#                 pass
# print('primes: ', primes)
# print('not_primes: ', not_primes)


# for i in numbers:
#     for j in range(1, i + 1):
#         if j != 1 and j != i and i % j == 0:
#             not_primes.append(i)
#         if i % 1 == 0 and i % i == 0 and i != 1:
#             primes.append(i)
# print('primes: ', primes)
# print('not_primes: ', not_primes)

# for i in numbers:
#     for j in range(1, i):
#         if i % j == 0 and i != j and j != 1:
#             not_primes.append(i)
#         else:
#             primes.append(i)
# print('primes: ', primes)
# print('not_primes: ', not_primes)

# for i in numbers:
#     if i <= 1:
#         pass
#     for j in range(2, int(i**0.5) + 1):
#         if i % i == 0:
#             not_primes.append(i)
#         primes.append(i)
# print('primes', primes)
# print('not_primes', not_primes)
