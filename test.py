import unittest
import hangman

class hangmanTestCase(unittest.TestCase):

    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer('tac','cat')
        self.assertTrue(answer)

    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer('ta','cat')
        self.assertEqual(answer,False)

    def test_checkWrongAnswer(self):
        answer = hangman.checkWrongAnswer('a','bb')
        self.assertEqual(answer,False)


if __name__ == "__main__":
    unittest.main()