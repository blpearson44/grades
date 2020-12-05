import klass


class Semester:
    def __init__(self, term, gpa, *klasses, total_units=0):
        self.term = term
        self.gpa = gpa
        self.klasses = klasses
        self.total_units = total_units

    def printInfo(self):
        print(self.term + " GPA: " + str(round(self.calculateGPA(), 3)) +
              " Units: " + str(self.total_units))
        for i in self.klasses:
            i.printInfo()

    def calculateGPA(self):
        gp = 0
        self.total_units = 0
        for i in self.klasses:
            gp += i.calculateGP()
            self.total_units += i.units
        self.gpa = gp/self.total_units
        return self.gpa
