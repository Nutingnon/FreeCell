from Cards import *

import random
# the class Deck is to simulate a deck of cards.


class Deck:
    def __init__(self, value_start, value_end, number_of_suits):
        self.deck = []
        self.start = value_start
        self.end = value_end

        for suit_id in range(1, int(number_of_suits)+1):
            for value in range(self.start, int(self.end)+1):
                card = Card(suit_id, value)
                self.deck.append(card)

# This function is to get the length of the deck.
    def get_length(self):
        return len(self.deck)

# This function can get a single card from a deck or a little deck of cards from a deck
    def get_card(self, n, m=0):
        if m == 0:
            m = n+1
        else:
            m = m+1
        card_list = self.deck[n:m]
        return card_list

# This function is to shuffle the cards sequence in the deck
    def shuffle(self):
        random.shuffle(self.deck)

# This function can add a card in deck.
    def add_card(self, suit_id, face_value):
        temp_card = Card(suit_id, face_value)
        if temp_card not in self.deck:
            self.deck.append(temp_card)
        else:
            print("This card has been in deck")

# This function is to draw a card from a deck, if the card exist, the card will be removed, if not, it will
        # reminds user that the card does not exist.

    def draw_card(self, suit_id, face_value):
        temp_card = Card(suit_id, face_value)
        if temp_card in self.deck:
            self.deck.remove(temp_card)
            return temp_card

        else:
            print("The card you want to draw doesn't exist in the current deck")

    def __str__(self):
        a = []
        for i in self.deck:
            a.append(str(i))
        return str(a)
