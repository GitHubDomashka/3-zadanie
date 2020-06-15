#Увеличить все отрицательные элементы на 5, а положительные уменьшить на 1
import random

items = [random.randint(-20,20) for i in range(0,20)]
print(items)

for i in items:
    if i>0:
        items[items.index(i)]=i-1
    else:
        items[items.index(i)]=i+5    
       
print(items)
