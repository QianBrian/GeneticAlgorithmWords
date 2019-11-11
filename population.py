from random import choice
from random import randint
from individual import Individual
from math import floor


class Population:

    # randomly generate the first population with constraints
    def __init__(self, phrase, capacity, length, mutrate):

        self.phrase = phrase
        self.length = length
        self.capacity = capacity
        self.mutRate = mutrate
        self.pop = []
        self.nextPop = []
        self.generationCount = 0
        self.currentHigh = ''
        self.bestMatch = ''
        self.goal = False
        ascii = range(32, 127)  # pool of ascii characters

        for i in range(int(capacity)):
            name = ''
            for j in range(length):
                name = name + chr(choice(ascii))  # add characters to individual reaching set length of phrase

                if self.goalTest(name):
                    self.goal = True

            self.pop.append(Individual(name, self.length, self.phrase))  # add phrases to population

        if self.goal:
            print('Desired phrase found in generation 1.')

    # checks if individual from population matches desired phrase
    def goalTest(self, name):

        if name == self.phrase:
            return True
        return False

    def getGoal(self):
        return self.goal

    def reproduction(self):

        self.generationCount += 1
        # do for every individual in a population
        for i in range(self.capacity):

            # crossover event
            parent1, parent2 = self.selection()
            child = parent1

            # evenly split "DNA" between two parents
            for j in range(floor(self.length/2) - 1):
                child[j*2] = parent2[j*2]

            # mutation event
            final = Individual(self.mutation(child, self.mutRate), self.length, self.phrase)

            # replace currently highest fitness individual
            if final.getFitness() > self.currentHigh:
                self.bestMatch = final.getName()

            # insert individual into new population
            self.nextPop.append(final)
        self.pop = self.nextPop  # set next gen population to current population
        self.currentHigh = max(self.nextPop)
        return "Generation count: " + str(self.generationCount)

    def selection(self):
        pool = []

        # adds individuals to gene pool based on their fitness level
        for i in range(len(self.pop)):
            for j in range(self.pop[i].getFitness()):
                pool.append(self.pop[i])

        parent1 = choice(pool)
        parent2 = choice(pool)

        while parent1.getName() == parent2.getName():
            parent2 = choice(pool)

        return parent1, parent2

    def mutation(self, dna, rate):
        mutated = dna
        if randint(0, 100) < rate:
            mutated[randint(0, self.length-1)] = ord(choice(ascii))
        return mutated
