s = []
for _ in range(5):
    string = input()
    s.append(string)
n=[]
for i in range(5):
    if 'HAFEZ' in s[i] or 'MOLANA' in s[i]:
        n.append(i+1)
if len(n)==0:
    n.append('NOT FOUND!')

print(*n)

