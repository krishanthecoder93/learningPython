import unittest
import math_op

class TestMath_op(unittest.TestCase):

    def test_add_number(self):
        self.assertEqual(math_op.add_number(2,3),5)
        self.assertEqual(math_op.add_number(1,3),4)
    
        

    def test_sub_number(self):
        self.assertEqual(math_op.sub_number(-4,-3),-1)
        self.assertEqual(math_op.sub_number(6,-3),9)
    
        

    def test_mul_number(self):
        self.assertEqual(math_op.mul_number(2,-3),-6)
        self.assertEqual(math_op.mul_number(12,-3),-36)
 
        

    def test_div_number(self):
        self.assertEqual(math_op.div_number(12,-3),-4)
        self.assertEqual(math_op.div_number(-21,-3),7)
   

if __name__=='__main__':
    unittest.main()

