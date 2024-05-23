n=int(input())

for i in range(n+1):
    space=' '*(n-i+1)
    star="*"*(2*i-1)
    print(space+star)

print('*'*(2*n+1))

for i in range(n,-1,-1):
    space=' '*(n-i+1)
    star="*"*(2*i-1)
    print(space+star)
