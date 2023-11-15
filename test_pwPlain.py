import unittest

from PythonPlain import validPassword1

class testPassword(unittest.TestCase):
    def testValidPW(self):
        self.assertTrue(validPassword1("Peterjas04!"))
        self.assertTrue(validPassword1("PJAS04!@"))
        self.assertTrue(validPassword1("PETERJOHAN@")) 
    
    def testLengthPW(self):
        self.assertFalse(validPassword1("Pijo4!")) # Length less than 8
        self.assertFalse(validPassword1("Piiiiiiiijoooo0!")) # Length more than 15
        
    def testInvalidCharacterPW(self):
        self.assertFalse(validPassword1("peterjohan04@")) # No Capital Letter
        self.assertFalse(validPassword1("47563743!")) # No Capital letter
        self.assertFalse(validPassword1("Peterjohan04")) # No Special Character
        self.assertFalse(validPassword1("peterjohan")) # all lower case, no capital letters or special characters
        self.assertFalse(validPassword1("12345434Ab")) # no special character
        self.assertFalse(validPassword1("12345434")) # only numbers
        self.assertFalse(validPassword1("47563743!")) # no alphabetical characters
        self.assertFalse(validPassword1("PeterJohan04^")) # Unaccepted Special Character
        
    def testSpecialPW(self):
        self.assertFalse(validPassword1("!Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("$Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("*Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("&Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("@Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("#Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("+Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("=Pijo0408")) # Special character in front
        self.assertFalse(validPassword1(")Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("/Pijo0408")) # Special character in front
        self.assertFalse(validPassword1("(Pijo0408")) # Special character in front

if __name__ == '__main__':
    unittest.main()