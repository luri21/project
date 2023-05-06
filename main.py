class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def say_hello(self):
        print(f"Hello, my name is {self.name} and my student ID is {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I teach {self.subject}")


class Engineer(Person):
    def __init__(self, name, age, gender, company):
        super().__init__(name, age, gender)
        self.company = company

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I work at {self.company}")
student = Student("Дем'ян", 12, "male", "S12345")
teacher = Teacher("Ігор", 24, "female", "Python")
engineer = Engineer("Peter", 40, "male", "Google")
student.say_hello()
teacher.say_hello()
engineer.say_hello()