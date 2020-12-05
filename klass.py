import grade


class Klass:
    def __init__(self, name, grade, units=3):
        self.name = name
        self.grade = grade
        self.units = units

    def calculateGP(self):
        if self.grade.calculatePercentage() > 92.5:
            return 4 * self.units
        elif self.grade.calculatePercentage() > 89.5:
            return 3.7 * self.units
        elif self.grade.calculatePercentage() > 86.5:
            return 3.3 * self.units
        elif self.grade.calculatePercentage() > 82.5:
            return 3 * self.units
        elif self.grade.calculatePercentage() > 79.5:
            return 2.7 * self.units
        elif self.grade.calculatePercentage() > 76.5:
            return 2.3 * self.units
        elif self.grade.calculatePercentage() > 72.5:
            return 2 * self.units
        elif self.grade.calculatePercentage() > 69.5:
            return 1.7 * self.units

    def __str__(self):
        return self.name
