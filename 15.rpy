import random
items = [random.randint(-20,20) for i in range(0,20)]
print(items)
items_1 = [random.randint(-20,20) for i in range(0,20)]
print(items_1)
x = []
for i in range(len(items)):
    for j in range(len(items[0])):
        x[i][j] = items[i][j] - items_1[i][j]
        x.append(x[i][j])
for r in x:
    print(r)