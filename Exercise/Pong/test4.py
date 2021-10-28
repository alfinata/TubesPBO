from test5 import Math

class Person:
    numberOfPeople = 0

    def __init__(self, name):
        self.name = name
        Person.addPerson()

    @classmethod
    def numberOfPeople_(cls):
        return cls.numberOfPeople

    @classmethod
    def addPerson(cls):
        cls.numberOfPeople += 1

p1 = Person("tim")

print(Person.numberOfPeople_())

p2 = Person("jill")

print(Person.numberOfPeople_())

print(Math.add5(5))