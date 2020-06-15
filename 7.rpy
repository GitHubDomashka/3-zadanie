import random
import math

items = [random.randint(-20,20) for i in range(0,20)]
print(items)

x=sum(items)/len(items)
print()
x=0
y=0
n=0
z=0
for i in items:
    if i>0:
        x+=i
        n+=1
    else:
        y+=i
        z+=1 
print("Сумма положительных чисел",x,"|","Сумма отрицательных чисел",y)
print("Количество положительных чисел",n,"|","Количество отрицательных чисел",z)

x1=x/n
y1=y/z
print("Ср.арифмет.положительных чисел",x1,"|","Ср.арифмет.отрицательных чисел",y1)