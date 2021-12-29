class human:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def introduce(self):
        print(f"my name is {self.name}")

    def askname(self, target):
        print(f"Me, {self.name} asks his name, and his name was {target.name}")


class student(human):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    
    def scores(self):
        print(f"my score is {self.grade}")

class firstGrader(student):
    def __init__(self, name, grade, kelas):
        super().__init__(name, grade)
        self.kelas = kelas

    def whatclass(self):
        print(f"my class is {self.kelas}")

class teacher(human):
    def __init__(self, name):
        super().__init__(name)
        self.salary = 100
    
    def showSalary(self):
        print(f"my salary is {self.salary}")

jojo = firstGrader("jojo", 90, "IF32")
dio = student("dio", 80)
uuf = teacher("hahaah")
uuf.showSalary()