import grade


class Klass:
    def __init__(self, name, grade=0, units=3):
        """ Initializes Klass object

        Args:
            name (string): name
            grade (float, optional): percentage grade
            units (int, optional): . Defaults to 3.
        """
        self.name = name
        self.grade = grade
        self.units = units

    def printInfo(self):
        """ Prints grade info """
        print(self.name + ": " + str(self.units) + " units")
        self.grade.printInfo()

    def calculateGP(self):
        """ Calculates GPA

        Returns:
            float: calculates gradepoints for class
        """
        if self.grade.calculatePercentage() > 92.5:
            return 4 * self.units
        elif self.grade.percentage > 89.5:
            return 3.7 * self.units
        elif self.grade.percentage > 86.5:
            return 3.3 * self.units
        elif self.grade.percentage > 82.5:
            return 3 * self.units
        elif self.grade.percentage > 79.5:
            return 2.7 * self.units
        elif self.grade.percentage > 76.5:
            return 2.3 * self.units
        elif self.grade.percentage > 72.5:
            return 2 * self.units
        elif self.grade.percentage > 69.5:
            return 1.7 * self.units

    def __str__(self):
        """ Returns name as string representatation

        Returns:
            string: name
        """
        return self.name
