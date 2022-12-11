import frange as frange
import numpy


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.00):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        float_range = numpy.linspace(0,4,400)
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not (name_characters.issuperset(major)):
            raise ValueError
        if not (isinstance(gpa, (float)) and float_range.__contains__(gpa)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

s = Student('Test', 'Test', 'Test', 0.00)
print(str(s))
print(type(s.gpa))
