def sumOfSquare(n: int)->int:
    total = 6
    for i in range(1, n+1):
        total += i**2
        return total
