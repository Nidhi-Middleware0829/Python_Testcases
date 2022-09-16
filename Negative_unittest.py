#This Programs tests whether two strings are equal or not using  negative unit testing

import unittest

class TestCase(unittest.TestCase) :
    def test_negative(self):
        a= "Jignesh"
        b="nidhi"
        # This will execute when a and b are not eqaul
        message = "These values are  not equal" 

        self.assertEqual(a,b,message)

if __name__ == '__main__':
    unittest.main()
