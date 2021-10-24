'''
    Loud implementation of modular functions
'''

def gcd(a: int, b: int, i: int = 1) -> int:
    '''
        Loud recursive implementation of the Euclidean Algorithm

        Parameters
        ----------

        a
            A number to find the gcd of with b
        b
            A number to find the gcd of with a
        i 
            Number of iterations of algorithm, default is 1
    '''

    if b > a:
        # Always keep b smaller than a
        a, b = b, a

    # Calculate remainder
    r = a % b
    # Quotient
    q = a // b

    print(f"({i}): {a} = {q}*{b} + {r}")

    if r == 0:
        # Base case
        print(f"\n({i}) implies the gcd is {b}")
        return b
    else:
        # Euclidean step
        # gcd(a, b) == gcd(b, r)
        return gcd(b, r, i + 1)