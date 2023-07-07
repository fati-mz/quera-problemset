def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
b = sum(int(digit) for digit in str(n))

count = 0
current_number = n + 1
while True:
    if is_prime(current_number):
        count += 1
        if count == b:
            print(current_number)
            break
    current_number += 1