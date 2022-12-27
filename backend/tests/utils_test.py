import unittest
from utils.generator import StrGenerator

class TestUtils(unittest.TestCase):

    def test_uniqueRandomString(self):
        givenStrings = ['abcd', 'abdc', 'ab32', 'Ab45']

        result = StrGenerator.generateRandomUniqueStrings(20, givenStrings)

        print(result)

if __name__ == '__main__':
    unittest.main()