import random
items = [random.randint(-20,20) for i in range(0,20)]
print(items)
x=0
for w in items:
    if w>0:
        x+=1

print("Количество чисел > 0 = ",x)
 