import unittest
import rpn 

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_sub(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_mult(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_div(self):
        result = rpn.calculate("15 3 /")
        self.assertEqual(5, result)
    def test_badInput(self):
        with self. assertRaises(TypeError):
            rpn.calculate('1 2 3 +')