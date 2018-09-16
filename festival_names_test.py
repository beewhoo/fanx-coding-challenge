import unittest

from festival_names_methods import *

class festival_names_test(unittest.TestCase):


    def test_unique_ordered(self):
        self.assertEqual(unique_ordered(['a','b','b','c']),['a','b','c'])

    def test_compare_lists(self):
        a =['a','b','c']
        b =['a','b','c','d']
        self.assertEqual(compare_lists(a,b),'a b c')

    def test_open_file(self):
        self.assertEqual(open_file('./data/test.txt'),['ab\n','cd\n'])





if __name__ == '__main__':
    unittest.main()
