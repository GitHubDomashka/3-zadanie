import random
items = [random.randint(-20,20) for i in range(0,20)]
print(items)
x=0
y=0
for w in items:
    if w>0:
        x+=1
    else:
        y+=1    
print("Количество положительных чисел",x)
print("Количество отрицательных чисел",y)    