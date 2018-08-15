# The card class is to simulate the real card. contains face, face_value, suit. suit_id
# The face_value is to calculalte the value of the card.
# The face attribute is to represent the face of card.( A, 2, 3, ..., J, Q, K.)
# The suit_id is introduced in order to handle the suit attribute more easily.


class Card:
    def __init__(self, suit_id, face_value):
        self.suit_id = suit_id
        self.face_value = face_value

        if self.face_value == 1:
            self.face = "Ace"

        elif self.face_value == 11:
            self.face = "Jack"

        elif self.face_value == 12:
            self.face = "Queen"

        elif self.face_value == 13:
            self.face = "King"

        elif 2 <= self.face_value <= 10:
            self.face = str(self.face_value)
        else:
            self.face = "ValueError"

        if self.suit_id == 1:
            self.suit = "Spade"
        elif self.suit_id == 2:
            self.suit = "Heart"
        elif self.suit_id == 3:
            self.suit = "Club"
        elif self.suit_id == 4:
            self.suit = "Diamond"
        else:
            self.suit = "SuitError"

        self.short_name = self.face[0] + ':' + self.suit[0]

        if self. face == '10':
            self.short_name = self.face + ':' + self.suit[0]

# overload the __eq__, which is used to judge whether two cards are equal.
    def __eq__(self, other):
        if self.suit == other.suit and self.face == other.face:
            return True
        else:
            return False

# This function is to get the card face value
    def get_value(self):
        return self.face_value

# This function is to get the card's suit_id
    def get_suitid(self):
        return self.suit_id

    def __str__(self):
        return self.short_name
