import random
items = [random.randint(0,20) for i in range(0,20)]
print(items)
x=0
y=0
for i in items:
    if i % 2 ==0:
        x+=i
    else:
        y+=i    
print("Сумма четных значений: {}".format(x))
print("Сумма нечетныхчетных значений: {}".format(y))