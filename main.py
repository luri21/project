class Student:
    def __init__(self, name, surfname, age ):
        self.name = name
        self.surfname = surfname
        self.age = age


s1 = Student("Oleg","Havron",25)
print(s1.name)
print(s1.surfname)
print(s1.age)