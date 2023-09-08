from datetime import datetime, timedelta

# خواندن ورودی‌ها
time_1 = datetime.strptime(input().strip(), '%H:%M:%S')
time_2 = datetime.strptime(input().strip(), '%H:%M:%S')

# محاسبه‌ی تفاضل دو زمان
if time_2 <= time_1:
    time_2 += timedelta(days=1)
diff = time_2 - time_1

# چاپ خروجی
# print(diff.strftime('%H:%M:%S'))

# تبدیل تفاضل زمان به ثانیه
total_seconds = diff.total_seconds()

# محاسبه‌ی ساعت، دقیقه و ثانیه‌ها
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# چاپ خروجی
print('{:02d}:{:02d}:{:02d}'.format(int(hours), int(minutes), int(seconds)))