import math
from decimal import Decimal

def pow(b, n):
    def even(n):
        if n%2==0:
            return 1
        return 0
    if n==0:
        return 1
    if even(n):
        return pow(b, n/2)**2
    return b*pow(b, n-1)

b,n = input().split()

print(pow(Decimal(b),int(n)))