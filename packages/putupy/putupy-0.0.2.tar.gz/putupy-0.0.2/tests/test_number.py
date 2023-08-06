import unittest


from putupy import base
from putupy.firstmodule import fmodule

class TestSimple(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(fmodule.add_one(5), 6)
    def test_add_two(self):
        self.assertEqual(base.add_two(5), 7)


if __name__ == '__main__':
    unittest.main()