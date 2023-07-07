n=int(input())

a=[i+1 for i in range(n)]

for j in range(1,n+1):
    print(*[i * j for i in a])