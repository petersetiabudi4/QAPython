import unittest

from PythonRegex import validPassword2

class testPassword(unittest.TestCase):
    
    def testValidPW(self): #Valid Passwords
        result = validPassword2("Haikalmzg03@")
        self.assertEqual(result, 0)
        result = validPassword2("HAIKALMZG@")
        self.assertEqual(result, 0)
        result = validPassword2("H!MZG123@")
        self.assertEqual(result, 0)
    
    def testLengthPW(self):
        result = validPassword2("Kall4!") # Length less than 8 
        self.assertEqual(result, -1)
        
        result = validPassword2("Haikalllllllllll0!") # Length more than 15
        self.assertEqual(result, -1)
        
    def testInvalidCharacterPW(self):
        result = validPassword2("haikalmsg03@") # No Capital Letters
        self.assertEqual(result, -1)
        
        result = validPassword2("45545454*") # No Capital Letters
        self.assertEqual(result, -1)
        
        result = validPassword2("hAikalmzg03") # No Special Characters
        self.assertEqual(result, -1)
        
        result = validPassword2("haikalmzg03") # No Capital Letters or Special Characters
        self.assertEqual(result, -1)
        
        result = validPassword2("1234asDAb") # No Special characters
        self.assertEqual(result, -1)
       
        result = validPassword2("12345678!@") # No Capital Letters
        self.assertEqual(result, -1)      
        
        result = validPassword2("12345678") # Only Numbers
        self.assertEqual(result, -1) 
        
        result = validPassword2("haikalmzg") # Only lowercase letters
        self.assertEqual(result, -1)   
        
        result = validPassword2("HaikalMZG04^") # Unnaccepted Special Character
        self.assertEqual(result, -1)   
        
        
    def testSpecialPW(self):
        result = validPassword2("!HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("$HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("*HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("&HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("@HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("#HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("+HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("=HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2(")HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("/HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
        
        result = validPassword2("(HaikalMzg03") # Special character in front
        self.assertEqual(result, -1)
    
if __name__ == '__main__':
    unittest.main()