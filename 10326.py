def simulate_chocolate_consumption(chocolates):
    # تعداد شکلات‌های خورده شده توسط هر فرد
    chocolates_eaten = [0, 0, 0, 0]
    
    # اندیس فرد در حال خوردن شکلات
    current_person = 0
    
    while True:
        # اگر شکلاتی در بخش جلوی فرد جاری وجود نداشته باشد، فرآیند تمام می‌شود
        if 0 in chocolates:
            break
        
        # فرد جاری یک شکلات می‌خورد
        chocolates[current_person] -= 1
        chocolates_eaten[current_person] += 1
        
        
        # چرخاندن ظرف شکلات به اندازه ۹۰ درجه در جهت عکس عقربه‌های ساعت
        chocolates = chocolates[1:4] + [chocolates[0]]
        
        # حرکت به نفر بعدی در جهت عقربه‌های ساعت
        current_person = (current_person + 1) % 4
    
    return chocolates_eaten

# دریافت ورودی
chocolates = list(map(int, input().split()))

# شبیه‌سازی فرآیند خوردن شکلات‌ها
result = simulate_chocolate_consumption(chocolates)

# چاپ نتیجه
print(*result)
