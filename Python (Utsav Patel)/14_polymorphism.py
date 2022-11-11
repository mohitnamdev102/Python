# polymorphism


class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def currency(self):
        print("Indian National Rupee is the currency of India.")

    def bird(self):
        print("Peacock is the National Bird of India.")


class Australia:
    def capital(self):
        print("Canberra is the capital of Australia.")

    def currency(self):
        print("Australian Dollar is the currency of Australia.")

    def bird(self):
        print("Emu is the National Bird of Australia.")


class USA:
    def capital(self):
        print("Washington D.C. is the capital of USA.")

    def currency(self):
        print("US Dollar is the currency of USA.")

    def bird(self):
        print("Eagle is the National Bird of USA.")


a = India()
b = Australia()
c = USA()

lis = [a, b, c]


for x in lis:
    x.capital()
    x.currency()
    x.bird()
    print("\n")

#.....................................................................

def some(a=None,b=None,c=None,d=None):

    if b==None and c==None and d==None:
        print(a)

    elif d== None and  c == None:
        print(a/b)

    elif d == None:
        print(a*b*c)

    else:
        print(a+b+c+d)

some(12,10,2,6)

#.....................................................................

# A simple Python function to demonstrate Polymorphism

def add(x, y, z = 0):
	return x + y+z

# Driver code
print(add(2, 3))
print(add(2, 3, 4))
