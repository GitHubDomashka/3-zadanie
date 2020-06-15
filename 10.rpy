import random

y=float(input("Введите число"))
items = [random.randint(-20,20) for i in range(0,20)]
print(items)
x=0
for w in items:
    if w>y:
        x+=1
    else:
        pass
if x==0:
    print("Ваше число больше возможного числа из списка")                     
print("Количество чисел > {} = ".format(y),x)
