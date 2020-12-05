class Grade:
    def __init__(self, categories=None, percentage=0):
        self.categories = categories
        self.percentage = percentage

    def calculatePercentage(self):
        self.percentage = 0
        for key in self.categories:
            self.percentage += self.categories[key][0] * \
                (sum(self.categories[key][1])/len(self.categories[key][1]))
        return self.percentage
