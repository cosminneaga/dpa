import random
import string


class StrGenerator:

    @staticmethod
    def generateRandomUniqueStrings(length, comparison):
        generatedString = ''.join(
            random.choices(
                string.ascii_letters +
                string.digits,
                k=length))
        check = StrGenerator.arrayContainsItem(generatedString, comparison)
        while check:
            generatedString = ''.join(
                random.choices(
                    string.ascii_letters +
                    string.digits,
                    k=length))
            check = StrGenerator.arrayContainsItem(generatedString, comparison)

        return generatedString

    @staticmethod
    def arrayContainsItem(item, array):
        for arrItem in array:
            if item == arrItem:
                return True
        return False

# givenStrings = ['abcd', 'abdc', 'ab32', 'Ab45']
# result = StrGenerator.generateRandomUniqueStrings(4, givenStrings)
# print(result)
