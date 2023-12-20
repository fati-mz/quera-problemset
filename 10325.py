


a,b = (map(int, input().split()))


print(*('Right',11-a,b) if b<=10 else ('Left',11-a,21-b))
