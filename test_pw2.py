import unittest

from PythonLibrary import validPassword2

class testPassword(unittest.TestCase):
    
    def testValidPW(self):
        result = validPassword2("Haikalmzg03@") # Valid Password
        self.assertEqual(result, 0)
    
    def testLengthPW(self):
        result = validPassword2("Kall4!") # length less than 8 
        self.assertEqual(result, -1)
        
        result = validPassword2("Haikalllllllllll0!") #length more than 15
        self.assertEqual(result, -1)
        
    def testCharacterPW(self):
        result = validPassword2("haikalmsg03@") #all lower case
        self.assertEqual(result, -1)
        
        result = validPassword2("haikalmzg03") #all lower case, no special character
        self.assertEqual(result, -1)
        
        result = validPassword2("haikalmzg@") #all lower case, no numbers
        self.assertEqual(result, -1)
        
        result = validPassword2("HAIKALMZG03@") #all uppercase
        self.assertEqual(result, -1)
        
        result = validPassword2("12345678Ab") #no special characters
        self.assertEqual(result, -1)
       
        result = validPassword2("12345678!@") #No Alphabet
        self.assertEqual(result, -1)      
        
        result = validPassword2("12345678") #Only Numbers
        self.assertEqual(result, -1)      
        
        
    def testSpecialPW(self):
        result = validPassword2("!HaikalMzg03") #special character in front
        self.assertEqual(result, -1)
    
if __name__ == '__main__':
    unittest.main()