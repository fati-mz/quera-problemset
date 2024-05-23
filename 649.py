def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# دریافت ورودی‌ها از کاربر
a = int(input())
b = int(input())

# پیدا کردن اعداد اول در بازه (a, b)
prime_numbers = []
for num in range(a + 1, b):
    if is_prime(num):
        prime_numbers.append(str(num))

# چاپ اعداد اول با جداکننده کاما
print(",".join(prime_numbers))
