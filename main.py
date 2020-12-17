from klass import Klass
from grade import Grade
from semester import Semester


def transform(object):
    """ Serializes objects for json format

    Args:
        object (Grade, Klass, or Semester): [object to be serialized]

    Raises:
        TypeError: [Raises TypeError if incompatible type is entered]

    Returns:
        [dict]: [dictionary to be used when dumped into json file]
    """
    if isinstance(object, Grade):
        return object.__dict__
    elif isinstance(object, Klass):
        return object.__dict__
    elif isinstance(object, Semester):
        return object.__dict__
    else:
        raise TypeError(
            "Only Grade, Klass, and Semester objects can be serialized.")


math_grade = Grade()
math_grade.categories = {"Homework": [
    0.15, [25, 96, 75, 83]], "Tests": [0.85, [100, 95, 87, 93]]}

math = Klass("Math", math_grade)

science_grade = Grade()
science_grade.categories = {"Homework": [
    0.15, [25, 13, 46, 19]], "Tests": [0.85, [115, 95, 83, 93]]}

science = Klass("Science", science_grade)

english_grade = Grade()
english_grade.categories = {"Homework": [
    0.15, [25, 13, 46, 19]], "Tests": [0.85, [115, 95, 83, 93]]}

english = Klass("English", english_grade)

klasses = [math, science, english]

semester = Semester("Fall 2020", 0, *klasses)

semester.printInfo()
