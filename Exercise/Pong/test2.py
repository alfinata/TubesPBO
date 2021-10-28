class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.maxStudents = max_students
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.maxStudents:
            self.students.append(student)
            return True
        return False

    def getAVG(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 80)
s3 = Student("Jill", 19, 75)

course = Course("Math", 2)
course.addStudent(s1)
course.addStudent(s2)

print(course.getAVG())
