class Grade:
    def __init__(self, categories=None, percentage=0):
        self.categories = categories
        self.percentage = percentage

    # calculates percentage and prints percentage and categories
    def printInfo(self, assignments=False):
        print(str(round(self.calculatePercentage(), 2)) + "%")
        for key in self.categories:
            if(len(self.categories[key][1]) > 0):
                avg = sum(self.categories[key][1])/len(self.categories[key][1])
                print(
                    key + " (" + str(self.categories[key][0]) + ") " + str(avg) + "% ")
            else:
                print(key + " (" + str(self.categories[key][0]) + ") " + " 0%")
            if assignments:
                print(self.categories[key])
        print()

    # calculates percentage, sets self.percentage, and returns self.percentage
    def calculatePercentage(self):
        self.percentage = 0
        for key in self.categories:
            if len(self.categories[key][1]) > 0:
                self.percentage += self.categories[key][0] * \
                    (sum(self.categories[key][1])/len(self.categories[key][1]))
        return self.percentage

    # prompts user to create the various categories and their weights,
    # assignments is left blank
    def createGrade(self):
        self.categories = {}
        numCategories = int(input("How many categories: "))
        for i in range(numCategories):
            category = str(
                input("What is the name of category " + str(i+1) + ": "))
            weight = float(
                input("What is the weight for this category? (n < 1): "))
            self.categories[category] = [weight, []]
        return self

    # prompts user to change the weights of the categories
    def changeWeight(self):
        for key in self.categories:
            weight = float(input("New weight for category " + key +
                                 "(" + str(self.categories[key][0]) + "): "))
            self.categories[key][0] = weight

    # prompts user to add categories
    def addCategories(self):
        answer = str(
            input("Would you like to change the weights of existing categories? (Y/N): "))
        if answer == "Y":
            self.changeWeight()
        numCategories = int(
            input("How many categories would you like to add: "))
        for i in range(numCategories):
            category = str(
                input("What is the name of category " + str(i+1) + ": "))
            if category in self.categories:
                print("Category already exists!")
            else:
                weight = float(
                    input("What is the weight for this category? (n < 1): "))
                self.categories[category] = [weight, []]

    # prompts user to add assignments
    def addAssignments(self):
        for key in self.categories:
            numAssignments = int(
                input("How many assignments for " + key + "?\n"))
            if numAssignments > 0:
                for i in range(numAssignments):
                    score = float(
                        input("Score for assignment " + str(i) + ": "))
                    self.categories[key][1].append(score)
