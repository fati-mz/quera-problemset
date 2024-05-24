num=int(input())

lamps=[]

for _ in range(num):
    lamps.append(input())

sum=0

for i in range(num-1):
    if lamps[i]!=lamps[i+1]:
        sum+=1

print(sum)
