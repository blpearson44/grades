from klass import Klass
from grade import Grade
from semester import Semester


math_grade = Grade()
math_grade.categories = {"Homework": tuple(
    (0.15, [25, 96, 75, 83])), "Tests": tuple((0.85, [100, 95, 87, 93]))}

math = Klass("Math", math_grade)

print(math.calculateGP())

science_grade = Grade()
science_grade.categories = {"Homework": tuple(
    (0.15, [25, 13, 46, 19])), "Tests": tuple((0.85, [115, 95, 83, 93]))}

science = Klass("Science", science_grade)

print(science.calculateGP())

english_grade = Grade()
english_grade.categories = {"Homework": tuple(
    (0.15, [25, 13, 46, 19])), "Tests": tuple((0.85, [115, 95, 83, 93]))}

english = Klass("English", english_grade)

print(english.calculateGP())

klasses = [math, science, english]

semester = Semester("Fall 2020", 0, *klasses)

print(semester.calculateGPA())
print(semester.gpa)
