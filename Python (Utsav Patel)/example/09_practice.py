a = [32,30,50,100]
print(a)
#remove a[1]
#a.remove(50)
#a.clear()
a.insert(4)
print(a)
a = (12,32,32,4,54,23,54,32,43,32)
a = list(a)
for x in a:
    if x == 32:
        temp = a.index(x)
        a.remove(x)
        a.insert(temp, 9)

a = tuple(a)
print(a)