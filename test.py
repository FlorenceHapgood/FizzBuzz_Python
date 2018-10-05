import unittest

from fizzbuzz import *

class Fizzbuzz(unittest.TestCase):

  def test_is_divisible_by_three_return_true(self):
    self.assertEqual(is_divisible_by_three(3), True)

  def test_is_divisible_by_three_return_false(self):
    self.assertEqual(is_divisible_by_three(4), False)

  def test_is_divisible_by_five_return_true(self):
    self.assertEqual(is_divisible_by_five(5), True)

  def test_is_divisible_by_five_return_false(self):
    self.assertEqual(is_divisible_by_five(6), False)

  def test_fizzbuzz_return_FizzBuzz(self):
      self.assertEqual(fizzbuzz(15), "FizzBuzz")

  def test_fizzbuzz_return_Fizz(self):
      self.assertEqual(fizzbuzz(3), "Fizz")

  def test_fizzbuzz_return_Buzz(self):
      self.assertEqual(fizzbuzz(5), "Buzz")

  def test_fizzbuzz_return_number(self):
      self.assertEqual(fizzbuzz(7), 7)

if __name__ == "__main__":
  unittest.main()
