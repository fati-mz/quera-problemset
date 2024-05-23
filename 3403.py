# دریافت ورودی‌ها از کاربر
numbers = []
for _ in range(4):
    num = int(input())
    numbers.append(num)

# محاسبه مجموع
sum_numbers = sum(numbers)

# محاسبه میانگین
average_numbers = sum_numbers / 4

# محاسبه حاصل ضرب
product_numbers = 1
for num in numbers:
    product_numbers *= num

# پیدا کردن بیشینه و کمینه
max_number = max(numbers)
min_number = min(numbers)

# چاپ نتایج با فرمت مشخص شده
print(f"Sum : {sum_numbers:.6f}")
print(f"Average : {average_numbers:.6f}")
print(f"Product : {product_numbers:.6f}")
print(f"MAX : {max_number:.6f}")
print(f"MIN : {min_number:.6f}")
