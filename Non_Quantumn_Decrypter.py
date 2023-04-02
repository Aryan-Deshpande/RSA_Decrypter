import time
import math
from sympy import symbols, simplify

a = 700 # primary number 1
b = 11 # primary number 2
mult = a*b
c = 8 # number that is not related to a and b

# create a decorator that will initialize the function with varibale ans
def init(func):
    def wrapper(*args, **kwargs):
        print("Initializing function")

        ans = None
        return func(ans, *args, **kwargs)
    return wrapper

# function that calculates the time taken for the function to run
def timing(func):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        func(*args, **kwargs)
        print("Time taken: ", time.time() - time1)
    return wrapper

# BRUTE FORCE, withought the use of generators
@init
def RSA(ans, mult, c) -> int:
    for i in range(1,1000000000000):
        exp = c**i
        if(exp%mult == 1):
            ans = i
            break
    return ans

# BRUTE FORCE, with the use of generators
@init
def RSA_Efficient(ans, mult, c) -> int:
    
    try:
        return next(i for i in range(1,10000000000000000) if (c**i)%mult == 1) 
    except StopIteration:
        return None


ans = RSA_Efficient(mult, c)
print(ans)
#print("Time taken: ", time.time() - sz, " time module withought decorator")

# Utilizes SymPy to simplify the equation
def equations() -> int:
    g, r, m ,n = symbols('g r m n')
    eq1 = ( ( g**(r/2) ) + 1 ) 

    values = {g:c, r:ans, m:1, n:mult}
    neweq1 = eq1.subs(values)

    eq1_subs = simplify(neweq1)
    return eq1_subs #, eq2_subs

# Efficient version of the equations function
def equations_efficient() -> int:
    eq1 = ( ( c**(ans/2) ) + 1 ) 
    return eq1

x = equations_efficient()

# Euclid's Algorithm
def euclids_algorithm(x) -> int:
    bool = True
    tempnumerator = x
    tempdenominator = mult
    temprem = tempnumerator%tempdenominator
    while(bool):
        
        temprem = tempnumerator%tempdenominator
        
        if((temprem) == 0): 
            bool = False
            return tempdenominator
        
        else:
            tempnumerator = tempdenominator 
            tempdenominator = temprem

    return 0

#
def euclids_algorithm_efficient(x) -> int:
    bool = True
    tempnumerator = x
    tempdenominator = mult
    temprem = tempnumerator%tempdenominator

    while(bool):
        
        temprem = tempnumerator%tempdenominator
        
        if((temprem) == 0): 
            bool = False
            return tempdenominator
        
        else:
            tempnumerator = tempdenominator 
            tempdenominator = temprem

    return 0

# implemented in C language, that makes it more efficient
def More_Efficient(x) -> int:
    return math.gcd(x, mult)

factor1 = More_Efficient(x)

def other_factor(factor1) -> int:
    return mult/factor1

factor2 = euclids_algorithm(x)
print(factor1)
