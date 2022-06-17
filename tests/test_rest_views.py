from ..app import rest_views
import unittest

class TestAvailable_Moves(unittest.TestCase):
    def test_get(self):
        test_request = rest_views.Available_Moves()
        test_request_get = test_request.get('pawn', 'a1')
        test_request_get_incorrect_figure = test_request.get('pret', 'a1')
        test_request_get_incorrect_field = test_request.get('pawn', 'a8')

        self.assertEqual(test_request_get,({'availableMoves': [['a2']], 'error': 'null', 'figure': 'pawn', 'currentField': 'a1'}, 200))
        self.assertEqual(test_request_get_incorrect_figure ,({'availableMoves': [], 'error': 'Figure does not exist.', 'figure': 'pret', 'currentField': 'a1'}, 404))
        self.assertEqual(test_request_get_incorrect_field, ({'availableMoves': [], 'error': 'Field does not exist.', 'figure': 'pawn', 'currentField': 'a8'}, 409))

class TestValidate_Move(unittest.TestCase):
    def test_get(self):
        test_request = rest_views.Validate_Move()
        test_request_get = test_request.get('queen', 'a1', 'a7')
        test_request_get_incorrect_figure = test_request.get('querl', 'a1', 'a2')
        test_request_get_incorrect_field = test_request.get('queen', 'a1', 'b5')

        self.assertEqual(test_request_get, ({'move': 'valid', 'figure': 'queen', 'error': 'null', 'currentField': 'a1', 'destField': 'a7'}, 200))
        self.assertEqual(test_request_get_incorrect_field, ({'move': 'invalid', 'figure': 'queen', 'error': 'Current move is not permitted.', 'currentField': 'a1', 'destField': 'b5'}, 409))
        self.assertEqual(test_request_get_incorrect_figure, ({'move': 'invalid', 'figure': 'querl', 'error': 'Current move is not permitted.', 'currentField': 'a1', 'destField': 'a2'}, 404))


if __name__ == '__main__':
    unittest.main()
