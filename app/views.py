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

