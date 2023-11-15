import unittest

from PythonNonLibrary import validPassword1

class testPassword(unittest.TestCase):
    def testValidPW(self):
        self.assertTrue(validPassword1("Peterjas04!"))
    
    def testLengthPW(self):
        self.assertFalse(validPassword1("Pijo4!"))
        self.assertFalse(validPassword1("Piiiiiiiijoooo0!"))
        
    def testCharacterPW(self):
        self.assertFalse(validPassword1("peterjohan04@")) #all lower case
        self.assertFalse(validPassword1("peterjohan04")) #all lower case, no special character
        self.assertFalse(validPassword1("peterjohan@")) #all lower case, no numbers
        self.assertFalse(validPassword1("PETERJOHAN04@")) #all uppercase
        self.assertFalse(validPassword1("12345434Ab")) #only numbers
        self.assertFalse(validPassword1("12345434")) #only numbers
        self.assertFalse(validPassword1("47563743!")) #no alphabetical characters
        
    def testSpecialPW(self):
        self.assertFalse(validPassword1("!Pijo0408")) #special character in front
    
if __name__ == '__main__':
    unittest.main()