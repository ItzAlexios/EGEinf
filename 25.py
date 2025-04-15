def check(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return 0
        
    return 1

for n in range(55_000_001, 60_000_001):
    for i in range(2, n):
        if n%i == 0 and check(i) and i%1000 == 777 and i != n:
                print(n, i)

import math

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, math.isqrt(n) + 1):
        if n % k == 0:
            return False
    return True

def f(limit=55_000_001):
    results = []
    i = limit
    # if limit == 55_000_662:
    #     print(results)
    while len(results) < 4:
        prime_divs = []
        for j in range(2, math.isqrt(i) + 1):
            if i % j == 0:
                if is_prime(j):
                    prime_divs.append(j)
                if j != i // j and is_prime(i // j):
                    prime_divs.append(i // j)
        
        if prime_divs:
           
            prime_divs = sorted(set(prime_divs))

            for m in prime_divs:
                if str(m)[-3:] == '777':
                    results.append((i, m))
                    print(i, m)
                
        i += 1

f()