import random
items = [random.randint(-20,20) for i in range(0,20)]
print(items)
x=1
y=1
for w in items:
    if w>0:
        x*=w
    else:
        y*=w    
print(x)
print(y)        