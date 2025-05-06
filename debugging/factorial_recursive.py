#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Calculates the factorial of a number recursively.
        The factorial of a number n is the product of all positive integers
        less than or equal to n.

    Parameters:
        n (int): The number for which to calculate the factorial.
                 Must be a positive integer or zero.

    Returns:
        int: The factorial of number n.
             Returns 1 if n = 0.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial_recursive.py <number>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)