def calculate_factorial(n :int) -> int: 
    """
    Calculate the factorial of a non-negative integer n using traditional while loop

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n (n!), defined as the product of all positive integers up to n.
             Returns 1 if n is 0, since 0! = 1.
    """
    if n == 0:
        return 1
    else: 
        factorial = n
        while n > 1:
            factorial *= (n-1)
            n -= 1
        return factorial  
