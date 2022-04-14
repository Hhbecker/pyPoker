

class Card(object):

    # map of ranks to cards 0=2, 1=3, ... 10=Q, 11=K, 12=A
    suitsDict = {0:'Spades', 1:'Clubs', 2:'Diamonds', 3:'Hearts'}
    ranksDict = {0:"2", 1:"3", 2:"4", 3:"5", 4:"6", 5:"7", 6:"8", 7:"9", 8:"10", 9:"J", 10:"Q", 11:"K", 12:"A"}

    def __init__(self, suit, rank):
        # check that both inputs are ints, suit is between 0-3, and rank is between 0-12
        if (suit >= 0 and suit <=3) and (rank >= 0 and rank <=12):
            self.suit = suit
            self.rank = rank

        else:
            raise ValueError("invalid input")

    def __str__(self):
        return 'rank: ' + self.ranksDict[self.rank] + ' suit: ' + self.suitsDict[self.suit]

    def __repr__(self):
        # Calling __str__() on a python list calls the __repr__ method on each element inside so...
        # When the deck __str__() method is called it calls the __repr__() method instead of __str__()
        return self.__str__()

    def __lt__(self, other):
        return self.rank < other.rank
