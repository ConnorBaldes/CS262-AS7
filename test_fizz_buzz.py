import unittest
import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz.fizz_buzz(),0)
        



if __name__ == '__main__':

    unittest.main(verbosity=2)