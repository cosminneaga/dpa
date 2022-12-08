class String:

    def generateRandomUniqueStrings(self, length, comparison):
        generatedString = ''.join(random.choices(string.ascii_letters+string.digits, k=length))
        check = self.arrayContainsItem(generatedString, comparison)
        while check == True:
            generatedString = ''.join(random.choices(string.ascii_letters+string.digits, k=length))
            check = self.arrayContainsItem(generatedString, comparison)

        return generatedString

    def arrayContainsItem(self, item, array):
        for arrItem in array:
            if item == arrItem:
                return True
        return False