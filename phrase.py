# individuals in population represented by phrases

class Phrase:

    def __init__(self, phrase, length):
        self.phrase = list(phrase)
        self.length = length

    def getPhrase(self):
        return self.phrase
    



test = 'hello world'
p1 = Phrase(test, len(test))