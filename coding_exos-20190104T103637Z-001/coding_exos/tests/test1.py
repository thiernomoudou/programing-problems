
import unittest
from package.a_test import perm, anagrams, binarygap


class TestMe(unittest.TestCase):

    def test_same_strings(self):
        result = perm('home', 'meho')
        self.assertEqual(result, True)

    def test_different_strings(self):
        result = perm('home', 'homc')
        self.assertEqual(result, False)

    def test_integer_with_strings(self):
        result = perm('home', 1)
        self.assertEqual(result, -1)

    def test_anagrams_with_small_letters(self):
        word_list = ['home', 'cat', 'tac', 'belong', 'ohme', 'meho', 'cool']
        result =  anagrams(word_list)
        self.assertEqual(len(result), 2)

    def test_anagrams_with_capital_letters(self):
        word_list = ['home', 'cat', 'tAc', 'belong', 'ohme', 'meho', 'cool']
        result =  anagrams(word_list)
        self.assertEqual(len(result), 2)


class BinaryGap(unittest.TestCase):

    def test_non_integer(self):
        result = binarygap('home')
        self.assertEqual(result, -1)

    def test_integer_nine(self):
        result = binarygap(9)
        self.assertEqual(result, 2)

    def test_integer_five_twenty_nine(self):
        result = binarygap(529)
        self.assertEqual(result, 4)

    def test_integer_twenty(self):
        result = binarygap(20)
        self.assertEqual(result, 1)

    def test_integer_fifteen(self):
        result = binarygap(15)
        self.assertEqual(result, 0)

    def test_integer_thirty_two(self):
        result = binarygap(32)
        self.assertEqual(result, 0)




if __name__ == '__main__':
    unittest.main()




# to run the test, type    python3 -m unittest tests/test1.py in the root directory

