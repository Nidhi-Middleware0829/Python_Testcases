# Python_Testcases
# For Positive_unitest: you have to run Python Positive_unittest.py 

python Positive_unittest.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

# For Negative_unittest: you have to run Python Negative_unittest.py

python Negative_unittest.py
F
======================================================================
FAIL: test_negative (__main__.TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python_testcases\Negative_unittest.py", line 12, in test_negative
    self.assertEqual(a,b,message)
AssertionError: 'Jignesh' != 'nidhi'
- Jignesh
+ nidhi
 : These values are  not equal

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
