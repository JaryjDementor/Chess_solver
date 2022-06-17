from flask_restful import Resource
from .views import Rook, Bishop, Queen, King, Knight, Pawn, check_figure_field


class Available_Moves(Resource):
    def get(self, figure, field):
        check_data = check_figure_field(figure, field)
        if check_data:

            if figure == "rook":
                list_moves = Rook(field, figure)
                available_moves_figure = list_moves.list_available_moves()

            elif figure == "bishop":
                list_moves = Bishop(field, figure)
                available_moves_figure = list_moves.list_available_moves()

            elif figure == "queen":
                list_moves = Queen(field, figure)
                available_moves_figure = list_moves.list_available_moves()

            elif figure == "king":
                list_moves = King(field, figure)
                available_moves_figure = list_moves.list_available_moves()

            elif figure == "knight":
                list_moves = Knight(field, figure)
                available_moves_figure = list_moves.list_available_moves()

            elif figure == "pawn":
                list_moves = Pawn(field, figure)
                available_moves_figure = list_moves.list_available_moves()

            else:
                available_moves_figure = []
            if not available_moves_figure:
                return {
                    "availableMoves": [],
                    "error": "Field does not exist.",
                    "figure": figure,
                    "currentField": field,
                }, 409
            else:
                return {
                    "availableMoves": [available_moves_figure],
                    "error": "null",
                    "figure": figure,
                    "currentField": field,
                }, 200
        else:
            return {
                "availableMoves": [],
                "error": "Figure does not exist.",
                "figure": figure,
                "currentField": field,
            }, 404


class Validate_Move(Resource):
    def get(self, figure, field, dest_field):
        check_data = check_figure_field(figure, field)
        if check_data:
            if figure == "rook":
                list_moves = Rook(field, figure)
                validate_move = list_moves.validate_move(dest_field)
            elif figure == "bishop":
                list_moves = Bishop(field, figure)
                validate_move = list_moves.validate_move(dest_field)
            elif figure == "queen":
                list_moves = Queen(field, figure)
                validate_move = list_moves.validate_move(dest_field)
            elif figure == "king":
                list_moves = King(field, figure)
                validate_move = list_moves.validate_move(dest_field)
            elif figure == "knight":
                list_moves = Knight(field, figure)
                validate_move = list_moves.validate_move(dest_field)
            elif figure == "pawn":
                list_moves = Pawn(field, figure)
                validate_move = list_moves.validate_move(dest_field)
            else:
                validate_move = []
            if not validate_move:
                return {
                    "move": "invalid",
                    "figure": figure,
                    "error": "Current move is not permitted.",
                    "currentField": field,
                    "destField": dest_field,
                }, 409
            else:
                return {
                    "move": "valid",
                    "figure": figure,
                    "error": "null",
                    "currentField": field,
                    "destField": dest_field,
                }, 200

        else:
            return {
                "move": "invalid",
                "figure": figure,
                "error": "Current move is not permitted.",
                "currentField": field,
                "destField": dest_field,
            }, 404
