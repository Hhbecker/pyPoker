import Card
import numpy

class Deck(object):

    def __init__(self):
        self.cards = []

        # initialize all cards with a nested for loop
        for x in range(4):
            for y in range(13):
                self.cards.append(Card.Card(x, y))

    def __str__(self):
        for i in self.cards:
            print(self.cards[i])

    def shuffle(self):
        ''' shuffles deck of cards '''

        indices = numpy.random.permutation(52)
        print(indices)
        # create a new list
        # generate a random permutation of the numbers 0-deck.length (could be less than 51 if shuffle is called during hand)
        # copy current deck indices to new locations based on permutation array





    # def popCard(self, num):
