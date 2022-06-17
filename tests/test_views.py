from ..app import views
import unittest


class TestCheckData(unittest.TestCase):
    def test_check_figure_field(self):
        figure_correct = "rook"
        figure_correct_incorrect = "rool"
        field_correct = "a1"
        field_correct_incorrect = "a9"
        self.assertEqual(
            views.check_figure_field(figure_correct, field_correct),
            [figure_correct, field_correct],
        )
        self.assertEqual(
            views.check_figure_field(figure_correct_incorrect, field_correct_incorrect),
            [],
        )


class TestFigure(unittest.TestCase):
    def test_letter_change_number_change_letter(self):
        test_change = views.Figure("a1", "pawn")
        test_letter_change_number = test_change.letter_change_number()
        test_number_change_letter = test_change.number_change_letter(
            [test_letter_change_number]
        )
        self.assertEqual(test_letter_change_number, "1.1")
        self.assertEqual(test_number_change_letter, ["a1"])

    def test_moves_rook(self):
        test_rook = views.Figure("a1", "rook")
        list_rook_moves = test_rook.moves_rook()
        self.assertEqual(
            list_rook_moves,
            [
                "a2",
                "a3",
                "a4",
                "a5",
                "a6",
                "a7",
                "a8",
                "b1",
                "c1",
                "d1",
                "e1",
                "f1",
                "g1",
                "h1",
            ],
        )

    def test_moves_bishop(self):
        test_bishop = views.Figure("a1", "bishop")
        list_bishop_moves = test_bishop.moves_bishop()
        self.assertEqual(list_bishop_moves, ["b2", "c3", "d4", "e5", "f6", "g7", "h8"])

    def test_list_available_moves(self):
        test_figure = views.Figure("d4", "king")
        list_king_moves = test_figure.list_available_moves()
        self.assertEqual(
            list_king_moves, ["c5", "e5", "e3", "c3", "c4", "d3", "e4", "d5"]
        )

    def test_validate_move(self):
        test_validate = views.Figure("d4", "knight")
        validate_moves_knight = test_validate.validate_move("b5")
        validate_moves_knight_incorrect = test_validate.validate_move("b1")
        self.assertEqual(validate_moves_knight, "b5")
        self.assertEqual(validate_moves_knight_incorrect, [])


if __name__ == "__main__":
    unittest.main()
