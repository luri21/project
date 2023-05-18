class Employee:
    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Position: {self.position}")

class Manager(Employee):
    def __init__(self, name, age, salary, position, subordinates):
        super().__init__(name, age, salary, position)
        self.subordinates = subordinates

    def display_info(self):
        super().display_info()
        print(f"Number of subordinates: {self.subordinates}")

class Developer(Employee):
    def __init__(self, name, age, salary, position, programming_language):
        super().__init__(name, age, salary, position)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

# Приклад використання
employee = Employee("John Smith", 30, 5000, "Employee")
employee.display_info()

print("-----")

manager = Manager("Alice Johnson", 40, 8000, "Manager", 5)
manager.display_info()

print("-----")

developer = Developer("Michael Davis", 35, 6000, "Developer", "Python")
developer.display_info()