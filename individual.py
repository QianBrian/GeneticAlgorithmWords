
class Individual:

    def __init__(self, name, length, phrase):
        self.name = name
        self.length = length
        self.phrase = phrase

    def getName(self):
        return self.name

    # determine the fitness for an individual in population
    def getFitness(self):
        fitness = 0
        for i in range(self.length):
            if self.phrase[i] == self.name:
                fitness += 1
        return fitness

