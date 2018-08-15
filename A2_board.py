# The Board class is to simulate the Board. with the empty value '-:-'
# The board size is 21*8. Because playing the NotFreeCell will not exceed this size.


class Board:
    def __init__(self):
        self.board = []
        self.empty = '-:-'
        for i in range(21):
            self.board.append([self.empty]*8)

# To decide how the board looks like
    def __str__(self):
        print_board = '\t\tOPEN___CELLS\t\t\t\t\t  OPEN_FOUNDATIONS\n\n'
        print_board += " 0\t\t 1\t\t 2\t\t 3\t\t 0\t\t 1\t\t 2\t\t 3\n"
        count = 0
        for row in self.board:
            count += 1
            for element in row:
                print_board = print_board + str(element) + '\t\t'
            print_board.strip('\t')
            print_board = print_board + '\n'
            if count == 1:
                print_board += '\n'
                print_board += '\t\t\t\t\t\t  Cascades\t\t\t\t\t\t\t'
                print_board += '\n\n'
                print_board += " 0\t\t 1\t\t 2\t\t 3\t\t 4\t\t 5\t\t 6\t\t 7\n"
            print_board.strip('\n')
        return print_board

# place a card on the board.
    def place_card(self, x, y, the_card):
        if x > 20 or y > 7:
            print("Illegal movement: outside of board.")
        else:
            self.board[x][y] = the_card

# remove the card in the board.
    def remove_card(self, x, y):
        if x > 20 or y > 7:
            return "Illegal movement: outside of board."
        elif str(self.board[x][y]) == '-:-':
            return "This place has been empty"
        else:
            self.board[x][y] = '-:-'
            print("The place", x, y, 'is clean now')

# detect if the position x,y is empty
    def is_empty(self, x, y):
        if 0 <= x <= 20 and 0 <= y < 8:
            if self.board[x][y] == '-:-':
                return True
            else:
                return False
        else:
            print("Outside of board, rookie!")

    def get_board(self):
        return self.board

# This function can move a card from a certain position to another position
    def move_card(self, card, from_x, from_y,  to_x, to_y):
        if from_x == '-:-' or from_y == '-:-':
            return "You cannot move a empty place!"
        elif to_x != '-:-' or to_y != '-:-':
            return "You cannot move card"
        else:
            self.board[from_x][from_y] = '-:-'
            self.board[to_x][to_y] = card
