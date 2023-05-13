class Employee:
    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

class Manager(Employee):
    def __init__(self, name, age, salary, position, num_subordinates):
        super().__init__(name, age, salary, position)
        self.num_subordinates = num_subordinates

class Developer(Employee):
    def __init__(self, name, age, salary, position, programming_language):
        super().__init__(name, age, salary, position)
        self.programming_language = programming_language
        manager = Manager("John Doe", 40, 50000, "Manager", 10)
        print(manager.name)
        print(manager.num_subordinates)

        developer = Developer("Jane Smith", 30, 60000, "Developer", "Python")
        print(developer.name)
        print(developer.programming_language)