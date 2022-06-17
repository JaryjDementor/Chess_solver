
def check_figure_field(figure, field):
    figures = ["bishop", "rook", "queen", "king", "knight", "pawn"]
    letters_board = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if figure in figures and field[0] in letters_board and len(field) ==2 and field[0].isalpha() and field[-1].isdigit() and 0<int(field[-1])<9:
        list_data = [figure, field]
        return list_data
    else:
        return []

class Figure():

    letters_board = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board = [str(i) + "." + str(j) for i in range(1, 9) for j in range(1, 9)]

    def __init__(self, field, figure):
        self.field = field
        self.figura = figure

    def letter_change_number(self): # example: a1 > 1.1; c1 > 3.1
        new_field = str(Figure.letters_board.index(self.field[0]) + 1) + "." + self.field[1:]
        return new_field

    def number_change_letter(self, list_moves): # example: 1.1 > a1; 3.1 > c1
        moves_list = []
        for i in list_moves:
            b = Figure.letters_board[int(i[0]) - 1] + i[-1]
            moves_list.append(b)
        return moves_list

    def moves_rook(self):
        number_field = Figure.letter_change_number(self)
        if number_field in Figure.board:
            list_moves = []
            for i in Figure.board:
                if number_field[0] == i[0] or number_field[-1] == i[-1]:
                    list_moves.append(i)
            list_moves.remove(number_field)
            available_moves = Figure.number_change_letter(self, list_moves)
            return available_moves

    def moves_bishop(self):
        number_field = Figure.letter_change_number(self)
        number_field_for_while = number_field

        list_moves = []
        while number_field_for_while in Figure.board:
            x = int(number_field_for_while[0])
            y = int(number_field_for_while[-1])
            new_number_field_for_while = str(x + 1) + "." + str(y + 1)
            if new_number_field_for_while in Figure.board:
                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while
            else:
                number_field_for_while = number_field
                break
        while number_field_for_while in Figure.board:
            x = int(number_field_for_while[0])
            y = int(number_field_for_while[-1])
            new_number_field_for_while = str(x - 1) + "." + str(y - 1)
            if new_number_field_for_while in Figure.board:
                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while
            else:
                number_field_for_while = number_field
                break
        while number_field_for_while in Figure.board:
            x = int(number_field_for_while[0])
            y = int(number_field_for_while[-1])
            new_number_field_for_while = str(x + 1) + "." + str(y - 1)
            if new_number_field_for_while in Figure.board:
                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while
            else:
                number_field_for_while = number_field
                break
        while number_field_for_while in Figure.board:
            x = int(number_field_for_while[0])
            y = int(number_field_for_while[-1])
            new_number_field_for_while = str(x - 1) + "." + str(y + 1)
            if new_number_field_for_while in Figure.board:
                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while
            else:
                number_field_for_while = new_number_field_for_while
                break

        available_moves = Figure.number_change_letter(self, list_moves)
        return available_moves

    def list_available_moves(self): #list_available_moves(),
        if self.figura == 'rook':
            available_moves_rook=Figure.moves_rook(self)
            return available_moves_rook

        if self.figura == 'bishop':
            available_moves_bishop = Figure.moves_bishop(self)
            return available_moves_bishop

        if self.figura == 'king':
            number_field = Figure.letter_change_number(self)
            list_moves = []
            list_cor = [
                [-1, 1],
                [1, 1],
                [1, -1],
                [-1, -1],
                [-1, 0],
                [0, -1],
                [1, 0],
                [0, 1],
            ]
            for i in list_cor:
                x = int(number_field[0]) + i[0]
                y = int(number_field[-1]) + i[1]
                cor_xy = str(x) + "." + str(y)
                if x != 0 and y != 0 and cor_xy in Figure.board:
                    list_moves.append(cor_xy)
            available_moves_king = Figure.number_change_letter(self, list_moves)
            return available_moves_king

        if self.figura == 'queen':
            list_moves_bishop = Figure.moves_bishop(self)
            list_moves_rook = Figure.moves_rook(self)
            for i in list_moves_rook:
                list_moves_bishop.append(i)
            return list_moves_bishop

        if self.figura == 'knight':
            number_field = Figure.letter_change_number(self)
            list_moves = []
            list_cor = [
                [-1, 2],
                [-2, 1],
                [-2, -1],
                [-1, -2],
                [1, -2],
                [2, -1],
                [2, 1],
                [1, 2],
            ]
            for i in list_cor:
                x = int(number_field[0]) + i[0]
                y = int(number_field[-1]) + i[1]
                cor_xy = str(x) + "." + str(y)
                if x != 0 and y != 0 and cor_xy in Figure.board:
                    list_moves.append(cor_xy)
                available_moves_knight = Figure.number_change_letter(self, list_moves)
            return available_moves_knight


        if self.figura == 'pawn':
            number_field = Figure.letter_change_number(self)
            if number_field in Figure.board and number_field[-1] != "8":
                list_moves = []
                y = int(number_field[-1]) + 1

                list_moves.append(number_field[:2] + str(y))
                available_moves_pawn = Figure.number_change_letter(self, list_moves)
                return available_moves_pawn
            else:
                return []

    def validate_move(self, dest_field):  # informującą, czymożliwy jest ruch na wskazane pole.
        if dest_field in Figure.list_available_moves(self):
            return dest_field
        else:
            return []


class Rook(Figure):
    pass

class Bishop(Figure):
    pass

class King(Figure):
    pass
class Queen(Figure):
    pass

class Knight(Figure):
    pass

class Pawn(Figure):
    pass
