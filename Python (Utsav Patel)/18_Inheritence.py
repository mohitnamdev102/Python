# Single Inheritance

class First:
    def one(self):
        print("This is my first class!")


class Second(First):
    def two(self):
        print("This is my second class!")

a = Second()
a.one()
a.two()


# Multilevel Inheritence

class First:
    def one(self):
        print("This is my first class!")


class Second(First):
    def two(self):
        print("This is my second class!")

class Third(Second):
    def third(self):
        print("Thi is my third class!")

a = Third()
a.one()
a.two()
a.third()


# Multiple Inheritence

class First:
    def one(self):
        print("This is my first class!")


class Second:
    def two(self):
        print("This is my second class!")

class Third(First, Second):
    def third(self):
        print("Thi is my third class!")

a = Third()
a.one()
a.two()
a.third()