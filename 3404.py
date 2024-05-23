# دریافت ورودی‌ها از کاربر
weight = int(input())
height = float(input())

# محاسبه BMI
bmi = weight / (height * height)

# چاپ مقدار BMI تا دو رقم اعشار
print(f"{bmi:.2f}")

# تشخیص وضعیت تناسب اندام بر اساس مقدار BMI
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
