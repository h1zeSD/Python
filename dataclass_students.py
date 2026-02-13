from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int


def info(student: Student):
    print(f"{student.name}, {student.age} лет, {student.grade} класс")

def increase_grade(student: Student):
    student.grade += 1

def is_adult(student: Student):
    if student.age >= 18:
        return True
    else:
        return False

def age_student_comparison(student1: Student, student2: Student):
    if student1.age > student2.age:
        print(f"{student1.name} старше")
    elif student1.age < student2.age:
        print(f"{student2.name} старше")
    else:
        print(f"{student2.name} и {student1.name} ровесники")

def is_classmates(student1: Student, student2: Student):
    if student1.grade == student2.grade:
        return True
    else:
        return False

def age_change(student: Student, age: int):
    student.age = age


student1 = Student("Иван", 14, 3)
student2 = Student("Мария", 13, 7)

info(student1)
info(student2)
