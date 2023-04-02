import math

# Extended Euclidean algorithm, where a and b are the numbers to find the GCD of, 
# and x and y are the coefficients of the linear combination of a and b that make up the GCD.
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

# Modular multiplicative inverse, where a and n are the numbers to find the inverse of,
# and n is the modulus.
def mod_inv(a, n):
    d, x, y = extended_gcd(a, n)
    if d != 1:
        raise ValueError("a is not invertible mod n")
    return x % n

# Chinese remainder theorem, where equations is a list of tuples (a, n) where a is the remainder,
# and hencee the number to be solved for, and n is the modulus.
def chinese_remainder_theorem(equations):
    N = math.prod(n for a, n in equations)
    x = sum(a * mod_inv(N // n, n) * (N // n) for a, n in equations)
    return x % N

# Factorize n into its prime factors.
def factorize(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.append(n)
    return factors

# Decrypt ciphertext using the Chinese remainder theorem.
def RSA_decrypt(ciphertext, public_key):
    n, e = public_key
    factors = factorize(n)
    equations = []
    for factor in factors:
        phi = (factor - 1) * (n // factor - 1)
        d = mod_inv(e, phi)
        equations.append((pow(ciphertext, d, factor), factor))
    plaintext = chinese_remainder_theorem(equations)
    return plaintext
