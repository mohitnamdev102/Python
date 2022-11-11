class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return self.fname + " " + self.lname


class EmployeeInfo(Employee):
    def __init__(self, fname, lname, age, id):
        Employee.__init__(self,fname, lname)
        self.age = age
        self.id = id


    def something(self, new):
        print("Employee Name is:", self.fullname())
        print("Employee Age is:", self.age)
        print("Employee Id is:", self.id)
        print("New is:", new)

a = EmployeeInfo("Utsav", "Patel", 28, 9)
a.something("hfd")