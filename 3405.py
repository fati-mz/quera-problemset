n=[]
while 1:
    b=int(input())
    if b==0:break
    else:
        n.insert(0,b)
print(*n,sep='\n')
