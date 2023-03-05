import unittest
from main import choice#, auth


class MyTestCase(unittest.TestCase):
    def test_choice_fail(self):
        self.assertEqual(choice(9), "Fail") #неверный выбор в меню
    def test_choice_faill(self):
        self.assertEqual(choice(9), "Fail")
    #def test_choice_close(self):
        #self.assertEqual(choice(0), None) #выход из меню
    def test_choice_name_branches(self):
        self.assertEqual(choice(4), 4) #произошел вывод из бд
    def test_choice_name_branchess(self):
        self.assertEqual(choice(4), 4)
    #def test_choice_book_cnt(self):
        #self.assertEqual(choice(6), 'Success') #произошел вывод из бд
    def test_choice_info_all(self):
        self.assertEqual(choice(3), 'Success') #произошел вывод из бд
    def test_choice_info_alll(self):
        self.assertEqual(choice(3), 'Success')
    #def test_auth_fail(self):
        #self.assertEqual(auth('id1','library'), 'auth Fail') #неудачная авторизация


if __name__ == '__main__':
    unittest.main()

