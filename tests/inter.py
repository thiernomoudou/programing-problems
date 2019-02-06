import unittest
from package.a_test import merge_count

class InterviewCake(unittest.TestCase):

    def test_merge_count(self):
       unsorted = [37, 89, 41, 65, 91, 53]
       highest_score = 100

       result = merge_count(unsorted, highest_score)
       expected = [91, 89, 65, 53, 41, 37]

       self.assertEqual(result, expected)
