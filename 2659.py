_=input()
m=input()
n=input()

i=0
for m,n in zip(m,n):
    if m!=n:i+=1

print(i)
