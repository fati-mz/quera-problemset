n=input()
g=n.count('G')
r=n.count('R')
y=n.count('Y')

if r>=3 or g==0 or y>=2 and r>=2:print('nakhor lite')
else:print('rahat baash')