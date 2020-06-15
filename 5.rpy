import random
items = [random.randint(-20,20) for i in range(0,20)]
print(items)
x=max(items)
y=min(items)
   
print("Max A[n] =",x,"[{}]".format(items.index(x)))
print("Min A[n] =",y,"[{}]".format(items.index(y)))        