import unittest
import task2


class TestTask2(unittest.TestCase):
    def test_super_digit_one(self):
        """Testing first sample digit"""
        self.assertEqual(task2.super_digit(9875), 2)
        self.assertEqual(task2.super_digit(-9875), "Invalid Input")
        self.assertEqual(task2.super_digit(5), 5)



    def test_super_digit_two(self):
        """Testing second sample digit"""
        self.assertEqual(task2.super_digit(1483), 7)
    def test_super_digit_extra(self):
        """Testing extra sample digit"""
        self.assertEqual(task2.super_digit(21), 3)
    def test_super_digit_invalid(self):
        self.assertEqual(task2.super_digit('test'),'Invalid Input')



if __name__ == '__main__':
    unittest.main()