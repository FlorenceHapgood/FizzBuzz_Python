import unittest

from fizzbuzz import *

class Fizzbuzz(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(hello_world(), 'hello world')

  def test_is_divisible_by_three(self):
    self.assertEqual(is_divisible_by_three(3), True)
    self.assertEqual(is_divisible_by_three(4), False)


  def test_is_divisible_by_five(self):
    self.assertEqual(is_divisible_by_five(5), True)
    self.assertEqual(is_divisible_by_five(6), False)


  def test_fizzbuzz(self):
      self.assertEqual(fizzbuzz(15), "FizzBuzz")
      self.assertEqual(fizzbuzz(3), "Fizz")
      self.assertEqual(fizzbuzz(5), "Buzz")
      self.assertEqual(fizzbuzz(7), 7)

if __name__ == "__main__":
  unittest.main()
