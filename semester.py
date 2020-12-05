import klass


class Semester:
    def __init__(self, term, gpa, *klasses, total_units=0):
        self.term = term
        self.gpa = gpa
        self.klasses = klasses
        self.total_units = total_units

    def calculateGPA(self):
        gp = 0
        self.total_units = 0
        for i in self.klasses:
            gp += i.calculateGP()
            self.total_units += i.units
        self.gpa = gp/self.total_units
        return self.gpa
