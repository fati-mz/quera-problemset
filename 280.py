a=[]
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a=sorted(a)

print('Yes' if a[2]**2==a[0]**2+a[1]**2 else 'NO')