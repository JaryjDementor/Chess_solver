from flask_restful import Resource
from .views_figure import Rook, Bishop, King, Queen, Knight, Pawn, str_to_class
from . import views


class Available_Moves(Resource):
    def get(self, figure, field, dest_field=None):
        check_data = views.check_figure_field(figure, field)
        available_moves_figure = []
        validate_move = None
        if check_data and len(check_data) == 2:
            class_figure = str_to_class(figure.title())
            class_figure = class_figure(field, figure)
            if not dest_field:
                available_moves_figure = class_figure.list_available_moves()
            else:
                validate_move = class_figure.validate_move(dest_field)

        else:
            respons = views.response(available_moves_figure, check_data, dest_field, figure, field, validate_move)

            return respons

        respons = views.response(available_moves_figure, check_data, dest_field, figure, field, validate_move)

        return respons

class Validate_Move(Available_Moves):
    pass