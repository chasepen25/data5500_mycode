
class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
    def increase_Salary(self):
        self.salary = self.salary * 1.10
    
employee1 = Employee("john",5000)
employee1.increase_Salary()
print(employee1.salary)