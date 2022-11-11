class Employee:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def fullname(self):
        return self.first_name + " " + self.last_name

class EmployeeDetails:
    def __init__(self, id, department):
        self.id = id
        self.department = department

class EmployeeInfo(Employee, EmployeeDetails):
    def __init__(self, first_name, last_name, phone, id, department, post, salary):
        Employee.__init__(self, first_name, last_name, phone)
        EmployeeDetails.__init__(self, id, department)
        self.post = post
        self.salary = salary


    def some(self):
        print("Employee Name is", self.fullname())
        print("Employee Phone Number is", self.phone)
        print("Employee id Number is", self.id)
        print("Employee Department is", self.department)
        print("Employee Post is", self.post)
        print("Employee Salary is", self.salary)

a = EmployeeInfo("Utsav", "Patel", 123456789, 9, "Python", 'Software Engineer', 50000)
a.some()