# import math

a,b=map(int,input().split())

# print(math.gcd(a,b),math.lcm(a,b))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a*b) // gcd(a, b)

print(gcd(a,b),lcm(a,b))
