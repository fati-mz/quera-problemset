m=list(map(int,input().split()))
n=[1,1,2,2,2,8]
for i in range(len(n)):
    n[i]=n[i]-m[i]
print(*(n))

# x=[]
# for item1, item2 in zip(list1, list2):
#     x .append( item1 - item2)
    