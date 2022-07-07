from flask_restful import Resource
from .views import *

class Available_Moves(Resource):
    def get(self, figure, field, dest_field=None):
        check_data = check_figure_field(figure, field)
        available_moves_figure = []
        validate_move = None
        if check_data and len(check_data) == 2:
            if figure == "rook":
                rook = Rook(field, figure)
                if not dest_field:
                    available_moves_figure = rook.list_available_moves()
                else:
                    validate_move = rook.validate_move(dest_field)
            elif figure == "bishop":
                bishop = Bishop(field, figure)
                if not dest_field:
                    available_moves_figure = bishop.list_available_moves()
                else:
                    validate_move = bishop.validate_move(dest_field)
            elif figure == "queen":
                queen = Queen(field, figure)
                if not dest_field:
                    available_moves_figure = queen.list_available_moves()
                else:
                    validate_move = queen.validate_move(dest_field)
            elif figure == "king":
                king = King(field, figure)
                if not dest_field:
                    available_moves_figure = king.list_available_moves()
                else:
                    validate_move = king.validate_move(dest_field)
            elif figure == "knight":
                knight = Knight(field, figure)
                if not dest_field:
                    available_moves_figure = knight.list_available_moves()
                else:
                    validate_move = knight.validate_move(dest_field)
            elif figure == "pawn":
                pawn = Pawn(field, figure)
                if not dest_field:
                    available_moves_figure = pawn.list_available_moves()
                else:
                    validate_move = pawn.validate_move(dest_field)


        else:
            response = ret(available_moves_figure, check_data, dest_field, figure, field, validate_move)

            return response

        response = ret(available_moves_figure, check_data, dest_field, figure, field, validate_move)

        return response

class Validate_Move(Available_Moves):
    pass