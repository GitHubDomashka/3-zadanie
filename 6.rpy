import random
import math

items = [random.randint(-20,20) for i in range(0,20)]
print(items)

for w in items:
    if w>0:
        items.append(w)
    else:
        w=w*(-1)
        items.append(w)

print(items)

 