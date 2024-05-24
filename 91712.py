x1, x2=map(int, input().split())

dif=x1-x2

if dif == 0:
    print('Saal Noo Mobarak!')
elif dif > 0:
    print('L'*dif)
else:
    print('R'*abs(dif))
