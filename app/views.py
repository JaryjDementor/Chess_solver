import sys

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

def check_figure_field(figure, field):
    list_data = []
    figures = ["bishop", "rook", "queen", "king", "knight", "pawn"]
    letters_board = ["a", "b", "c", "d", "e", "f", "g", "h"]

    if figure in figures:
        list_data.append(figure)

    if field[0] in letters_board and len(field) == 2 and field[0].isalpha() and field[
        -1].isdigit() and 0 < int(field[-1]) < 9:
        list_data.append(field)

    return list_data

def response(aval, data, dest_field=None, figure=None, field=None, validate_move=None):
    code_error = None
    error = None
    move = 'invalid'
    if not dest_field:
        if figure in data and field in data:
            error = 'null'
            code_error = 200
        elif len(data) == 1:
            if field in data:
                error = "Figure does not exist."
                code_error = 404
            else:
                error = "Field does not exist."
                code_error = 409
        else:
            error = "Field and figure does not exist."
            code_error = 404

        return {
            "availableMoves": aval,
            "error": error,
            "figure": figure,
            "currentField": field
        }, code_error
    else:
        if len(validate_move) != 0:
            code_error = 200
            move = 'valid'
        else:
            code_error = 409
            error = "Current move is not permitted."

        return {"move": move,
                "figure": figure,
                "error": error,
                "currentField": field,
                "destField": dest_field,
               }, code_error


class Figure:

    letters_board = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board = [str(i) + "." + str(j) for i in range(1, 9) for j in range(1, 9)]

    def __init__(self, field, figure):
        self.field = field
        self.figura = figure


    def letter_change_number(self):  # example: a1 > 1.1; c1 > 3.1
        new_field = (
            str(Figure.letters_board.index(self.field[0]) + 1) + "." + self.field[1:]
        )
        return new_field

    def number_change_letter(self, list_moves):  # example: 1.1 > a1; 3.1 > c1
        moves_list = []
        for i in list_moves:
            b = Figure.letters_board[int(i[0]) - 1] + i[-1]
            moves_list.append(b)
        return moves_list

    def list_available_moves(self):  # list_available_moves(),
        pass

    def validate_move(self, dest_field):  # informującą, czymożliwy jest ruch na wskazane pole.
        if dest_field in self.list_available_moves():
            return dest_field
        else:
            return []


class Rook(Figure):
    def list_available_moves(self):
        number_field = Figure.letter_change_number(self)
        if number_field in Figure.board:
            list_moves = []
            for i in Figure.board:
                if number_field[0] == i[0] or number_field[-1] == i[-1]:
                    list_moves.append(i)
            list_moves.remove(number_field)
            available_moves = Figure.number_change_letter(self, list_moves)
            return available_moves


class Bishop(Figure):
    def list_available_moves(self):
        super().list_available_moves()
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


class King(Figure):
    def list_available_moves(self):

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


class Queen(Figure):
    def list_available_moves(self):
        bishop = Bishop(self.field, self.figura)
        rook = Rook(self.field, self.figura)
        list_moves_bishop = bishop.list_available_moves()
        list_moves_rook = rook.list_available_moves()
        for i in list_moves_rook:
            list_moves_bishop.append(i)
        return list_moves_bishop

class Knight(Figure):
    def list_available_moves(self):
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


class Pawn(Figure):
    def list_available_moves(self):
        number_field = Figure.letter_change_number(self)
        if number_field in Figure.board and number_field[-1] != "8":
            list_moves = []
            y = int(number_field[-1]) + 1

            list_moves.append(number_field[:2] + str(y))
            available_moves_pawn = Figure.number_change_letter(self, list_moves)
            return available_moves_pawn
        else:
            return []