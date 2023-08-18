def sieve(n: int):
    """
    check if the given input is prime or not
    parameter
    ---------
    n   :   int
    
    return  :   boolean
                True if the given input is a prime,
                otherwise False
    """

    # any 2 is the smallest prime number.
    # every even number has a divisor 2. so no even
    # number is prime
    if n < 2 or n > 2 and n % 2 == 0:
        return False
    
    # only odd numbers are checking from 3 to sqrt(n).
    # if a number is composite number then it must have
    # a divisor less or equal to sqrt(n)
    i = 3
    while (i * i <= n): # i * i <= n -> i <= sqrt(n)
        if n % i == 0:
            return False
        i += 2 # 3 -> 5 -> 7 -> 9. . . . . 
    return True
