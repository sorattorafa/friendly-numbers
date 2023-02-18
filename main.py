    
import time

def sum_proper_divisors(n, div_sums, primes):
    """Retorna a soma dos divisores próprios de um número n"""
    if n in div_sums:
        return div_sums[n]
    if n in primes:
        div_sums[n] = 1
        return div_sums[n]
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    div_sums[n] = sum(divisors)
    return div_sums[n]

def find_friendly_pairs(limit):
    """Encontra todos os pares de números friendly menores ou iguais a um limite"""
    pairs = []
    div_sums = {}
    primes = [2]
    for n in range(3, limit+1, 2):
        if all(n % p != 0 for p in primes[:int(n**0.5)//2]):
            primes.append(n)
        m = sum_proper_divisors(n, div_sums, primes)
        if n < m and m <= limit and m == sum_proper_divisors(n, div_sums, primes):
            pairs.append((n, m))
    return pairs

start_time = time.time()

pairs = find_friendly_pairs(100000)

print(pairs)

print("Tempo de execução:", time.time() - start_time, "segundos")
