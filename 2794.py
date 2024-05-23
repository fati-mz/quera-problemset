from collections import Counter

def find_unique_element(lst):
    # شمارش تعداد تکرار هر عنصر در لیست
    count = Counter(lst)
    # یافتن عنصری که فقط یک بار ظاهر شده است
    for item, freq in count.items():
        if freq == 1:
            return item
    return None  # اگر عنصری که فقط یک بار ظاهر شده باشد وجود نداشته باشد

x=[]
y=[]
for _ in range(3):
    a,b=input().split()
    x.append(a)
    y.append(b)

print(find_unique_element(x)+' '+find_unique_element(y))
