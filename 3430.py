s=input()

for i in range(len(s)):
    n=s[i:]
    m=s[i]*i
    s = m + n
    print(s)
