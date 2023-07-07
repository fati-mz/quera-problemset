a=input()
n=[int(i) for i in a]
for i in range(len(n)):
    print(f'{n[i]}: {str(n[i])*(n[i])}')