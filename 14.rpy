#Создать новый массив из двух других массивов путём:
import random
items = [random.randint(-20,20) for i in range(0,20)]
print(items)
items_1 = [random.randint(-20,20) for i in range(0,20)]
print(items_1)
x=[0,20]
for i in items and items_1:
    x[i]=items[i]-items_1[i]

    print(x)