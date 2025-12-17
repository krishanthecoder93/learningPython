import unittest
import math_op_class

class TestCalculate(unittest.TestCase):

    def test_add_number(self):
        calculate = math_op_class.Calculate()
        self.assertEqual(calculate.add_number(4,5),9)

    def test_sub_number(self):
        calculate = math_op_class.Calculate()
        self.assertEqual(calculate.sub_number(4,5),-1)

    def test_mul_number(self):
        calculate = math_op_class.Calculate()
        self.assertEqual(calculate.mul_number(4,5),20)

    def test_div_number(self):
        calculate = math_op_class.Calculate()
        self.assertEqual(calculate.div_number(40,5),8)



if __name__=='__main__':
    unittest.main()