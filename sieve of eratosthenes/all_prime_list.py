def all_prime_list(n: int) -> list:
    """
    generate a list of numbers where prime numbers are
    marked as True and composite numbers are marks as
    False
    parameter
    ---------
    n   :   int
            range. all prime number from 1 to n
    
    return
    ------
    list
    list of prime numbers
    
    time complexity     :   O(n log log n)
    space complexity    :   O(n)
    """
    # store the prime numbers. considering all number as
    # prime (True)
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False

    # marking all the even numbers as False
    for i in range(4, n + 1, 2):
        primes[i] = False
        i += 2
    
    # marking all the factors of odd prime numbers
    i = 3
    while (i * i <= n):
        if primes[i]:
            for p in range(i * 2, n + 1, i):
                primes[p] = False
        i += 2
    return primes

