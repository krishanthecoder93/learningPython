import unittest
import math_op_class
import sys

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = math_op_class.Calculate()


    def tearDown(self):
        del self.calculate
    @unittest.skip("Addition feature temporarily disabled")
    def test_add_number(self):
         self.assertEqual(self.calculate.add_number(4,5),9)



    @unittest.skipIf(sys.version_info<(3,10),"Requires Pyhton 3.10 or higher")
    def test_sub_number(self):
        self.assertEqual(self.calculate.sub_number(4,5),-1)



    @unittest.skipUnless(sys.platform.startswith("win32"),"Runs only on windows")
    def test_mul_number(self):
        self.assertEqual(self.calculate.mul_number(4,5),20)



    def test_div_number(self):
        self.assertEqual(self.calculate.div_number(40,5),8)
        with self.assertRaises(ValueError):
            self.calculate.div_number(10,0)



if __name__=='__main__':
    unittest.main()