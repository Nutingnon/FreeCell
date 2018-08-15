# The NotFreeCell class is the game class, which contains the key points that the game needs.
from A2_Deck import *
import A2_board
import time


class NotFreeCell:

    def __init__(self):
        self.open_cells = ["-:-"]*4
        self.open_foundation = [["-:-"], ["-:-"], ["-:-"], ["-:-"]]
        self.cascades = []
        self.deck = Deck(1, 13, 4)
        self.deck.shuffle()
        self.cardboard = A2_board.Board()
        card_deck = self.deck.get_card(0, 52)
        n = 0

        # This for loop is to place the card into the board
        for x in range(1, 8):
            for y in range(0, 8):
                if (x, y) == (7, 4):
                    return
                else:
                    self.cardboard.place_card(x, y, card_deck[n])
                    n += 1

    # The get_length function is to get the length of a slot. the length represents how many cards a certain slot has.

    def get_length(self, slot):
        if 0 <= slot < 8:
            len_x = 1
            while True:
                if str(self.cardboard.board[len_x][slot]) != '-:-':
                    len_x += 1
                else:
                    return len_x - 1

        else:
            print("The slot you  want to check is outside of board. Learn the rule first, please.")

    # This function is to check the rule within the cascades
    # After careful observation, I find that the suit_id can be used properly to develop this suit rule.

    def chk_suit_rule(self, card1, card2):
        if card1.suit_id + card2.suit_id in [3, 5, 7]:
            return True
        else:
            return False

    # This function is to check the rule of moving card.

    def chk_value_rule(self, card1, card2):
        if card1.face_value == (card2.face_value - 1):
            return True
        else:
            return False

# The foundation rule is to check whether the card is legal for place into foundation. if it is legal, place it.
        # and this function will automatically decide which position the legal card should be put.
    def foundation_rule(self, card):
        if card.suit_id == 1:
            if card.face_value == len(self.open_foundation[0]):
                self.open_foundation[0].append(card)
                return True
            else:
                print("Come on, You must obey the rule of moving cards to foundation.")
                return False

        elif card.suit_id == 2:
            if card.face_value == len(self.open_foundation[1]):
                self.open_foundation[1].append(card)
                return True
            else:
                print("Come on, You must obey the rule of moving cards to foundation.")
                return False

        elif card.suit_id == 3:

            if card.face_value == len(self.open_foundation[2]):
                self.open_foundation[2].append(card)
                return True
            else:
                print("Come on, You must obey the rule of moving cards to foundation.")
                return False

        elif card.suit_id == 4:
            if card.face_value == len(self.open_foundation[3]):
                self.open_foundation[3].append(card)
                return True
            else:
                print("Come on,You must obey the rule of moving cards to foundation.")
                return False

        else:
            print("illegal suit")
            return False

    # This function is to move a card to foundation
    # the  parameter slot is to let the user input which slot he/she wants to take the card.
    # naturally, the card will at the end of the slot.

    def mv_to_foundation(self, slot):
        if 0 <= slot < 8:
            if self.get_length(slot) == 0:
                print("You cannot move the empty box, rookie!!!")
            else:
                mv_card = self.cardboard.board[self.get_length(slot)][slot]
                print(mv_card)
                if self.foundation_rule(mv_card):
                    self.cardboard.remove_card(self.get_length(slot), slot)
                    for i in range(4):
                        self.cardboard.board[0][4 + i] = self.open_foundation[i][-1]
                else:
                    print("read the rule please.")
                    return False

        else:
            print("outside of board, please check the rule first")

    # This function is to move card from cascades to opencell.

    def mv_to_opencell(self, slot):
        place = False
        if 0 <= slot < 8:
            if self.get_length(slot) == 0:
                print("You cannot move the empty box, rookie!!!")
            else:
                mv_card = self.cardboard.board[self.get_length(slot)][slot]
                # check whether there is an available space in open cells
                for i in range(4):
                    if str(self.cardboard.board[0][i]) == '-:-':
                        self.cardboard.board[0][i] = mv_card
                        self.cardboard.remove_card(self.get_length(slot), slot)
                        place = True
                        break

                if not place:
                    print("The open cells is full, you cannot move any extra card into it.")
        else:
            print("outside of board, Google the rules please.")

    # This function is to move card within the cascades.

    def mv_card(self, slot1, slot2):
        if 0 <= slot1 < 8 and 0 <= slot2 < 8:
            slot1 = int(slot1)
            slot2 = int(slot2)
            # get the card that to be moved.
            if self.get_length(slot1) != 0:
                # str(self.cardboard.board[self.get_length(slot1)+1][slot1]) != '-:-':
                moving_card = self.cardboard.board[self.get_length(slot1)][slot1]

            # Judge whether the slot2 is a empty slot. the variable chkslot means 'check slot'
                chkslot = self.get_length(slot2)
                if chkslot == 0:
                    self.cardboard.board[1][slot2] = moving_card
                    self.cardboard.remove_card(self.get_length(slot1), slot1)

                else:
                    goal_card = self.cardboard.board[self.get_length(slot2)][slot2]
                    if self.chk_suit_rule(moving_card, goal_card) and self.chk_value_rule(moving_card, goal_card):
                        self.cardboard.remove_card(self.get_length(slot1), slot1)
                        self.cardboard.board[self.get_length(slot2)+1][slot2] = moving_card
                    else:
                        print("If a card is placed on a cascade, it must be placed of a card of the opposite colour,",
                              "and of a suit that is one higher than itself.")

            else:
                print("You cannot move an empty box!!!!!")
        else:
            print("Do you want to move the card to outer space? You have to comply with the rule!")

    # This function is used to move card from open foundation to cascades

    def mv_from_foundation(self, f_line, slot):
        if 0 <= f_line < 3 and 0 <= slot < 8:
            if self.open_foundation[f_line] == ['-:-']:
                print("You cannot move the empty foundation.")
                return False
            else:
                if self.get_length(slot) == 0:
                    mv_card = self.open_foundation[f_line].pop()
                    self.cardboard.board[1][slot] = mv_card

                    for i in range(4):
                        self.cardboard.board[0][4 + i] = self.open_foundation[i][-1]

                else:
                    mv_card = self.open_foundation[f_line].pop()
                    goal_card = self.cardboard.board[self.get_length(slot)][slot]
                    if self.chk_value_rule(mv_card, goal_card) and self.chk_suit_rule(mv_card, goal_card):
                        self.cardboard.board[self.get_length(slot)+1][slot] = mv_card
                        for i in range(4):
                            self.cardboard.board[0][4 + i] = self.open_foundation[i][-1]
                    else:
                        self.open_foundation[f_line].append(mv_card)
                        print("Read the game rule first, baby")
                        return False
        else:
            print("Outside of board")
            return False

    # This function is used to move card from open cell to cascades

    def mv_from_opencell(self, c_line, slot):
        if 0 <= c_line <= 3 and 0 <= slot <= 7:
            if str(self.cardboard.board[0][c_line]) == '-:-':
                print("You cannot move an empty cell")
                return False
            else:
                mv_card = self.cardboard.board[0][c_line]
                if self.get_length(slot) == 0:
                    self.cardboard.board[1][slot] = mv_card
                    self.cardboard.board[0][c_line] = '-:-'
                    return True

                else:
                    goal_card = self.cardboard.board[self.get_length(slot)][slot]
                    if self.chk_value_rule(mv_card, goal_card) and self.chk_suit_rule(mv_card, goal_card):
                        self.cardboard.board[self.get_length(slot)+1][slot] = mv_card
                        self.cardboard.board[0][c_line] = '-:-'
                        return True
                    else:
                        print("Read the game rule first, baby")
                        return False
        else:
            print("Outside of the board, please be careful with rules")
            return False

    # This function is used to automatically move card from cascades to foundation once it reaches a certain condition

    def auto_collect(self):
        # First of all, check if there is one or more empty foundation.
        for i in range(4):
            if str(self.open_foundation[i][-1]) == '-:-':
                print("Auto collection fails because there exist (an) empty foundation")
                return False

            else:
                continue

        # the variable judge_auto is to judge the condition to keep taking card from cascades to foundation automatically.
        judge_auto = 1
        while judge_auto == 1:
            temp_foundation = self.open_foundation
            for i in range(4):
                for j in range(8):

                    # judge if there is a suitable card in 8 cascades that can be moved to a certain foundation.
                    if self.get_length(j) == 0:
                        continue
                    elif self.open_foundation[i][-1].face_value == self.cardboard.board[self.get_length(j)][j].face_value - 1:
                        mv_card = self.cardboard.board[self.get_length(j)][j]
                        self.open_foundation[i].append(mv_card)
                        self.cardboard.remove_card(self.get_length(j), j)

            if temp_foundation == self.open_foundation:
                judge_auto = 0
            else:
                continue

    # This function is to judge whether the game can end up with win.
    def judge_win(self):
        if len(self.open_foundation[0]) == len(self.open_foundation[1]) == len(self.open_foundation[2]) == \
                len(self.open_foundation[3]) == 14:
            print("Congratulations! YOU WIN!!!!!!!!")
            return True

        else:
            return False

    def __str__(self):
        return str(self.cardboard)


def main():
    play = True
    print("Welcome to my new exciting solitaire game -- Not FreeCell !!!!!")
    time.sleep(1)
    print("First of all, let's read some basic rules:")
    time.sleep(1)
    print("1. Only one card may be moved at aa time.")
    print("2. The four foundations must be built starting from the Ace of the appropriate suit, followed by the 2, then the \
    3 etc. Until the King is placed")
    print("3. If a card is placed on a cascade, it must be placed of a card of the opposite colour, and of a value that is \
    one higher than itself. E.g. a red 2 can be placed on a black3, but not black 4")
    print("4. Any card may be placed in an empty cascade")

    print("5. Cards from the foundations may be placed back onto a cascade, or an empty cascade slot.")
    print("6. Only one card at a time can occupy a cell slot.")
    print("7. Victory is achieved when all four foundations are filled with their respective suits from Ace to King.")
    print("For more details, please look up in the documentation file. \nNow, let's Start!!!")
    print()
    print()
    game = NotFreeCell()
    time.sleep(3)
    print(game)
    while play:
        user_idea = input("""
        What do you want to do?
        rg = restart the game
        a = move a card from one cascade slot to another
        s = move a card from a certain cascade slot to open cells
        d = move a card from a certain cascade slot to open foundations
        f = move a card from open cells to a cascade slot
        w= move a card from open foundation to a cascade slot
        e = automatically move valid cards from cascades to open foundation.
        q = quit the game.
        """)
        if user_idea == 'q':
            print("Defeat")
            play = False
            return play
        elif user_idea == 'a':
            while True:
                try:
                    slot1 = int(input("Which slot do you want to move the card from?"))
                    slot2 = int(input("Which slot do you want to move the card to?"))
                    break
                except ValueError:
                    print("Never try to let this program crash, young man.")

            game.mv_card(slot1, slot2)
            print(game)

        elif user_idea == 's':
            while True:
                try:
                    slot1 = int(input("Which slot do you want to move the card from?"))
                    break
                except ValueError:
                    print("Never try to let this program crash, young man.")

            game.mv_to_opencell(slot1)
            print(game)

        elif user_idea == 'd':
            while True:
                try:
                    slot1 = int(input("Which slot do you want to move the card from?"))
                    break
                except ValueError:
                    print("Never try to let this program crash, young man.")

            game.mv_to_foundation(slot1)
            print(game)

        elif user_idea == 'f':
            while True:
                try:
                    slot1 = int(input("Which slot of open cells do you want to move the card from?"))
                    slot2 = int(input("Which slot of cascades do you want to move the card to?"))
                    break
                except ValueError:
                    print("Never try to let this program crash, young man.")

            game.mv_from_opencell(slot1, slot2)
            print(game)

        elif user_idea == 'w':
            while True:
                try:
                    slot1 = int(input("Which slot of foundations do you want to move the card from?"))
                    slot2 = int(input("Which slot of cascades do you want to move the card to?"))
                    break
                except ValueError:
                    print("Never try to let this program crash, young man.")

            game.mv_from_foundation(slot1, slot2)
            print(game)

        elif user_idea == 'e':
            game.auto_collect()
            print(game)

        elif user_idea == 'rg':
            print("Defeat!!!!!!")
            main()
        else:
            print("Do not try to let this game crash, fledgeling!")

        if game.judge_win():
            play = False
            return play

if __name__ == "__main__":
    main()
