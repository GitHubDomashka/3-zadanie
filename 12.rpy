#Увеличить все нечётные элементы массива на 3, а чётные в 2 раза
import random

items = [random.randint(-20,20) for i in range(0,20)]
print(items)

for i in items:
    if i % 2==0:
        items[items.index(i)]=i*2
    else:
        items[items.index(i)]=i+3    
       
print(items)