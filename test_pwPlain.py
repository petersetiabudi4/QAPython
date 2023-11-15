import unittest

from PythonPlain import validPassword1

class testPassword(unittest.TestCase):
    def testValidPW(self):
        self.assertTrue(validPassword1("Haikalmzg03@"))
        self.assertTrue(validPassword1("HAIKALMZG@"))
        self.assertTrue(validPassword1("Kall4!")) 
    
    def testLengthPW(self):
        self.assertFalse(validPassword1("Kall4!")) # Length less than 8
        self.assertFalse(validPassword1("Haikalllllllllll0!")) # Length more than 15
        
    def testInvalidCharacterPW(self):
        self.assertFalse(validPassword1("haikalmsg03@")) # No Capital Letter
        self.assertFalse(validPassword1("hAikalmzg03")) # No Special Character
        self.assertFalse(validPassword1("haikalmzg03")) # No capital letters or special characters
        self.assertFalse(validPassword1("12345678")) # only numbers
        self.assertFalse(validPassword1("haikalmzg")) # only lowercase letters
        self.assertFalse(validPassword1("HaikalMZG04^")) # Unaccepted Special Character
        
    def testSpecialPW(self):
        self.assertFalse(validPassword1("!HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("$HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("*HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("&HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("@HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("#HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("+HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("=HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1(")HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("/HaikalMzg03")) # Special character in front
        self.assertFalse(validPassword1("(HaikalMzg03")) # Special character in front

if __name__ == '__main__':
    unittest.main()