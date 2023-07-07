a=input()
b=input()
m=int(a[::-1])
n=int(b[::-1])

if a==b:print(f'{a} = {b}')
elif m<n:print(f'{a} < {b}')
else:print(f'{b} < {a}')