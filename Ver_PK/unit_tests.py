import unittest
from my_fun import retion_student_books, expenses


class MyTestCase(unittest.TestCase):
    def test_retion_1(self):
        self.assertEqual(retion_student_books(30,200), 0.15) #неверный выбор в меню
        print("OK")

    def test_expenses_1(self):
        self.assertEqual(expenses(100,300), 30000) #неверный выбор в меню
        print("OK")

    def test_retionl_2(self):
        self.assertEqual(retion_student_books(100,20), 5) #неверный выбор в меню
        print("OK")

    def test_expenses_2(self):
        self.assertEqual(expenses(80,300), 24000) #неверный выбор в меню
        print("OK")


if __name__ == '__main__':
    test = MyTestCase()
    test.test_retion_1()
    test.test_expenses_1()
    test.test_retionl_2()
    test.test_expenses_2()
