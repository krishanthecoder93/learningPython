class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        return f"{self.name} works at {Employee.company_name} with salary {self.salary}"

emp1 = Employee("Alice", 60000)
emp2 = Employee("Bob", 70000)

print(emp1.show())
print(emp2.show())

print("-------------------------------------------")

Employee.company_name = "InnoTech"

print(emp1.show())
print(emp2.show())

print("-------------------------------------------")


emp1.company_name = "Freelancer Inc."   # creates instance attribute

print(emp1.company_name)
print(emp2.company_name)
print(Employee.company_name)
