def draw_line(spaces, stars):
    line = spaces + stars + spaces + spaces + stars + spaces
    print(line)

def draw_diamonds(n):
    # نیمه بالایی لوزی‌ها
    for i in range(n // 2 + 1):
        spaces = ' ' * (n // 2 - i)
        stars = '*' * (2 * i + 1)
        draw_line(spaces, stars)
    
    # نیمه پایینی لوزی‌ها
    for i in range(n // 2 - 1, -1, -1):
        spaces = ' ' * (n // 2 - i)
        stars = '*' * (2 * i + 1)
        draw_line(spaces, stars)

# دریافت ورودی
n = int(input())
draw_diamonds(n)
