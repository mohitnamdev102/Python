a = int(input("Please enter the level: "))
for x in range(1, a+1):
    print("*"*x)


n = int(input("Please enter the length: "))

# a = "*****"
a = "*"*(n+1)
l = []
for x in range(n):
    s = a[x:n]
    s = " ".join(s)
    print(s)
    s = s.center((2*n)-1)
    l.append(s)

print(l)
print("\n".join(l[:0:-1]+l))

n = int(input("Please enter the length: "))
a = "*"*(n+1)
# a = "abcdefghijklmnopqrstuvwxyz"

l = []
for x in range(n):
    s = a[x:n]
    s = s[:0:-1]+ s
    s = " ".join(s)
    s = s.center((4*n)-3)

    l.append(s)

print("\n".join(l[:0:-1]+l))
