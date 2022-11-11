class Hello:

    def __init__(self, name,  framework):
        self.name = name
        self.framework = framework


    def some(self):
        print("Hello",self.name)

    def other(self, age, course):
        print("Hello", self.name)
        print("You are", age)
        print("You are learning", course, self.framework)

    def kuchbhi(self):
        print("hello", self.name)
        print("you will learn",self.framework)


a = Hello("Utsav", "Django")

a.some()
a.other(28,"Python")
a.kuchbhi()


'''
# inheritence
# operator overloding
# function overloading
# polymorphism
# abstraction
'''