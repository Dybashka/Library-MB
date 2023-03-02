import unittest
from main import choice


class MyTestCase(unittest.TestCase):
    def test_choice_fail(self):
        self.assertEqual(choice(9), "Fail")  # проходит
    def test_choice_close(self):
        self.assertEqual(choice(0), None)  # проходит
    def test_choice_name_branches(self):
        self.assertEqual(choice(4), "Right")

    #def test_choice_book_cnt_fail(self):
    #    self.assertEqual(choice(6), 9, None)
    #def test_choice_book_cnt(self):
    #    self.assertEqual(choice(6), "Количество книг = 22 ")  #
        # def test_choice_info_all(self):
    # self.assertEqual(choice(3), "Вывод каждой строки и ее столбцов") # no


if __name__ == '__main__':
    unittest.main()
