def max_divisions(n):
    # تقسیم تعداد جاده‌ها به دو بخش تقریبا مساوی
    horizontal_roads = n // 2
    vertical_roads = n - horizontal_roads
    
    # محاسبه تعداد بخش‌ها
    max_sections = (horizontal_roads + 1) * (vertical_roads + 1)
    return max_sections

# دریافت ورودی
n = int(input())

# محاسبه و چاپ بیشترین تعداد قسمت‌های ممکن
print(max_divisions(n))
