num= int(input())
max_letter=0

for _ in range(num):
    name=input()
    len_name=len(set(name))
    if len_name > max_letter :
        max_letter=len_name
        
print(max_letter)
