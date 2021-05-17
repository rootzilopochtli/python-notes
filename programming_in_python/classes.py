# 15. Classes
# class
class Car:

    def __init__(self,name,gear,miles):
        self.name = name
        self.gear = gear
        self.miles = miles

    def drive(self,miles):
        self.miles = self.miles + miles
    def shift_gear(self,gear):
        self.gear = gear
car = Car("Tesla", 0, 0)
car.shift_gear(6)
del car
#print(car.gear)

# object oriented programming
# inheritence
# employee
# common class is called the parent
class Employee:
    def __init__(self, name, age, dob, job_description):
        self.name = name
        self.age = age
        self.dob = dob
        self.job_description = job_description
    def get_salary(self):
        print("salary printend")
# child class
class Manager(Employee):
    def __init__(self, name, age, dob, job_description, department, employees):
        super().__init__(name, age, dob, job_description)
        self.department = department
        self.employees = employees
    def add_employee(self):
        print("adding employee")
    def get_salary(self):
        print("salary printend for manager")

manager = Manager("kim", 28, "23-8-2000", "manages everything", "engineering department", 87)
manager.get_salary()
manager.add_employee()
