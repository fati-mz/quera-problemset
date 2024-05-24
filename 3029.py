# خواندن ورودی
x, _ = map(int, (input().split()))
x1, _ = map(int, (input().split()))

# محاسبه ضرب خارجی
cross_product = x - x1

# تعیین جهت چرخش
if cross_product > 0:
    print("Left")
else:
    print("Right")
