from ..app import views
import unittest

class TestCheckData(unittest.TestCase):

    def test_check_figure_field(self):
        figure_correct = 'rook'
        figure_correct_incorrect = 'rool'
        field_correct = 'a1'
        field_correct_incorrect = 'a9'
        self.assertEqual(views.check_figure_field(figure_correct,field_correct), [figure_correct, field_correct])
        self.assertEqual(views.check_figure_field(figure_correct_incorrect, field_correct_incorrect), [])

if __name__ == '__main__':
    unittest.main()
