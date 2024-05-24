# الگوهای پاسخ دهی
keyvoon_pattern = [3, 3, 1, 1, 2, 2]
nezam_pattern = [1, 2, 3]
shir_farhad_pattern = [2, 1, 2, 3]

# خواندن ورودی
N = int(input())
answers = input().strip()

# محاسبه نمرات
keyvoon_score = sum(1 for i in range(N) if int(answers[i]) == keyvoon_pattern[i % len(keyvoon_pattern)])
nezam_score = sum(1 for i in range(N) if int(answers[i]) == nezam_pattern[i % len(nezam_pattern)])
shir_farhad_score = sum(1 for i in range(N) if int(answers[i]) == shir_farhad_pattern[i % len(shir_farhad_pattern)])

# پیدا کردن بیشترین نمره
max_score = max(keyvoon_score, nezam_score, shir_farhad_score)

# پیدا کردن اسامی کسانی که بیشترین نمره را کسب کرده‌اند
winners = []
if keyvoon_score == max_score:
    winners.append("keyvoon")
if nezam_score == max_score:
    winners.append("nezam")
if shir_farhad_score == max_score:
    winners.append("shir farhad")

# چاپ نتیجه
print(max_score)
for winner in sorted(winners):
    print(winner)
