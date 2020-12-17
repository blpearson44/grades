class Grade:
    def __init__(self, categories=None, percentage=0):
        """Creates a Grade object

        Args:
            categories (list, optional): A list containing the categories. Defaults to None.
            percentage (int, optional): A float for the percentageA Defaults to 0.
        """
        self.categories = categories
        self.percentage = percentage

    def printInfo(self, assignments=False):
        """ Calculates percentage and prints the info for the object

        Args:
            assignments (bool, optional): Whether or not to include the assignments. Defaults to False.
        """
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

    def calculatePercentage(self):
        """ Calculates percentage, sets self.percentage, and returns self.percentage


        Returns:
            float: percentage
        """
        self.percentage = 0
        for key in self.categories:
            if len(self.categories[key][1]) > 0:
                self.percentage += self.categories[key][0] * \
                    (sum(self.categories[key][1])/len(self.categories[key][1]))
        return self.percentage

    def createGrade(self):
        """ Prompts user to create the various categories and their weights, assignments is left blank

        Returns:
            Grade : self
        """
        self.categories = {}
        numCategories = int(input("How many categories: "))
        for i in range(numCategories):
            category = str(
                input("What is the name of category " + str(i+1) + ": "))
            weight = float(
                input("What is the weight for this category? (n < 1): "))
            self.categories[category] = [weight, []]
        return self

    def changeWeight(self):
        """ Prompts user to change the weights of the categories """
        for key in self.categories:
            weight = float(input("New weight for category " + key +
                                 "(" + str(self.categories[key][0]) + "): "))
            self.categories[key][0] = weight

    def addCategories(self):
        """ Prompts user to add categories """
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

    def addAssignments(self):
        """ Prompts user to add assignments"""
        for key in self.categories:
            numAssignments = int(
                input("How many assignments for " + key + "?\n"))
            if numAssignments > 0:
                for i in range(numAssignments):
                    score = float(
                        input("Score for assignment " + str(i) + ": "))
                    self.categories[key][1].append(score)
