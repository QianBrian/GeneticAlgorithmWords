from population import Population

# main code

phrase = input('Type a phrase to begin evolution. ')
length = len(phrase)
capacity = int(input('Input population capacity. '))
mutrate = int(input('Input mutation rate, 1 - 100%. '))

launch = Population(phrase, capacity, length, mutrate)

while not launch.getGoal():
    launch.reproduction()
    print(launch.currentHigh)
    print(launch.bestMatch)
