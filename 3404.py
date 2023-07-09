m=int(input())
n=float(input())
b=round(m/n*n,2)


x = m/float(n*n)

# print("%.2f" % x)
# print("%.2f" % round(x, 2))
# print( "{:.2f}".format(round(13.949, 2)))
print(float(round(x,2)))

if x < 18.5:
    print('Underweight')
if x>=18.5 and x<25:
    print("Normal")
if x >= 25 and x < 30:
   print('Overweight')
if x >= 30:
   print('Obesity')