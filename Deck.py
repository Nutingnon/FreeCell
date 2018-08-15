from Cards import *

import random

class Deck:

    def __init__(self):
        self.deck = []
        for suit_id in range(1, 5):
            for face_value in range(1, 14):
                self.deck.append(Card(suit_id, face_value))
        self.foundations = [[]]*4

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        self.decklines = []
        for i in range(4):
            self.decklines.append(self.deck[7*i:7*i+7])
        for j in range(4,8):
            self.decklines.append(self.deck[6*i+4:6*i+10])
        # self.deckline1 = self.deck[0:7]
        # self.deckline2 = self.deck[7:14]
        # self.deckline3 = self.deck[14:21]
        # self.deckline4 = self.deck[21:28]
        # self.deckline5 = self.deck[28:34]
        # self.deckline6 = self.deck[34:40]
        # self.deckline7 = self.deck[40:46]
        # self.deckline8 = self.deck[46:52]

# The line1, line2 in add function means add the card from line1 to line2
    def add(self, line1, line2):
        temp_card = self.decklines[line1].pop()
        self.decklines[line2].append(temp_card)

    def draw(self,line_d):
        pass
        '''if card.suit == Spade:
                go to foundation[1]
                
            elif card.suit ==
            ...'''


    def __str__(self):
        self.deckshow = []
        for i in self.deck:
            self.deckshow.append(str(i))
        return str(self.deckshow)


deck1 = Deck()
print(deck1)