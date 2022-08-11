import unittest
import task1



class TestTask1(unittest.TestCase):
    def test_bigger_is_greater_first(self):
        """Testing first sample group"""
        self.assertEqual(task1.biggerIsGreater('ab'),'ba')
        self.assertEqual(task1.biggerIsGreater('a b'),'Invalid Input')

        self.assertEqual(task1.biggerIsGreater('bb'),'Not Arrangeable')
        self.assertEqual(task1.biggerIsGreater('hefg'),'hegf')
        self.assertEqual(task1.biggerIsGreater('dkhc'),'hcdk')

    def test_bigger_is_greater_second(self):
        """Testing second sample group"""
        self.assertEqual(task1.biggerIsGreater('lmno'),'lmon')
        self.assertEqual(task1.biggerIsGreater('dcba'),'Not Arrangeable')
        self.assertEqual(task1.biggerIsGreater('dcbb'),'Not Arrangeable')
        self.assertEqual(task1.biggerIsGreater('abdc'),'acbd')
        self.assertEqual(task1.biggerIsGreater('abcd'),'abdc')
        self.assertEqual(task1.biggerIsGreater('fedcbabcd'),'fedcbabdc')

    def test_bigger_is_greater_invalid(self):
        """Testing invalid inputs"""
        self.assertEqual(task1.biggerIsGreater('ab!'),'Invalid Input')
        self.assertEqual(task1.biggerIsGreater('ab23!'),'Invalid Input')
        self.assertEqual(task1.biggerIsGreater('adasd2adab!'),'Invalid Input')
        self.assertEqual(task1.biggerIsGreater('adasd   2adab!'),'Invalid Input')


if __name__ == '__main__':
    unittest.main()