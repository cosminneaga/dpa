import unittest
from utils.string import String

class TestUtils(unittest.TestCase):
    
    string = String.String()

    def test_uniqueRandomString(self):
        givenStrings = ['abcd', 'abdc', 'ab32', 'Ab45']

        result = string.generateRandomUniqueStrings(20, givenStrings)

        print(result)

if __name__ == '__main__':
    unittest.main()