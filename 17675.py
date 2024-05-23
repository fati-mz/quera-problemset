import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    # 5*n*+4 or 5*n*-4 are perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

num = int(input())

s=''

for i in range(1,num+1):
    if is_fibonacci(i):
        s+='+'
    else:
        s+='-'

print(s)
