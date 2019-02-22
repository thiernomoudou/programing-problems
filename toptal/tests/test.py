
import unittest
from package.toptal import capitalize_string

class HelloWorld(unittest.TestCase):

    def test_return_capitalize_sting(self):
       result = capitalize_string("this is a test... and another test.")
       expected = "This is a test... And another test."
       self.assertEqual(result, expected)







if __name__ == '__main__':
    unittest.main()


