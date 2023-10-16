# factors.py

import sys
import math

def factorize(n):
    for p in range(2, n + 1):
        if n % p == 0:
            q = n // p
            return f"{n}={p}*{q}"
    return f"{n}=1*{n}"

def main(input_file):
    with open(input_file, 'r') as file:
        numbers = file.read().splitlines()
    
    for number in numbers:
        n = int(number)
        factorization = factorize(n)
        print(factorization)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
