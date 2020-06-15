import random
items = [random.randint(0,20) for i in range(0,20)]
print(items)
x=0
for i in items:
    if i>9:
        x+=i
print(x)       