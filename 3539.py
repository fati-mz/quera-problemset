a=input()
i=len(a)
while i!=1:
    a=str(sum([int(d) for d in a]))
    i=len(a)
print(a)
