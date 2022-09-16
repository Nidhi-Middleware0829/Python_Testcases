#This Programs tests whether two strings are equal or not using  postive unit testing

import unittest

class TestCase(unittest.TestCase) :
    def test_positive(self):
        a= "gaurav"
        b="gaurav"
      # error message in case if test case got failed
        message = "These values are  not equal" 

        self.assertEqual(a,b,message)

if __name__ == '__main__':
    unittest.main()


