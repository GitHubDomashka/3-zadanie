#Вывести элементы массива, меньших среднего арифметического

import random
import math

items = [random.randint(-20,20) for i in range(0,20)]
items_1=[]
print(items)
print("-------------")
x=sum(items)/len(items)
print("Ср.арифмет. = ",x)
for i in items:
    if i<x:
        items_1.append(i)
    else:
        pass  
print("-------------")      
print(items_1)    