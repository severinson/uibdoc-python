import unittest
import submodule

from submodule.usefulstuff import find_min

class Tests(unittest.TestCase): # what does this mean?

    def test_useful_work(self): # function name important
        a = 1
        b = 2
        r = submodule.usefulstuff.do_useful_work(a, b)
        self.assertEqual(r, 3)
        return

    def test_find_min_1(self):
        self.assertEqual(find_min([1, 2, 3, 0]), 0)
        return

    def test_find_min_2(self):
        self.assertEqual(find_min([1001, 2000, 3000]), 1001)
        return

    def test_find_min_3(self):
        self.assertEqual(find_min({1001, 2000, 3000}), 1001)
        return

    def test_find_min_4(self):
        with self.assertRaises(ValueError):
            find_min([])
        return
