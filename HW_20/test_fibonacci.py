import unittest

from HW_20.fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self) -> None:
        self.fibonacci = Fibonacci()

    def test_fibonacci_computation(self):
        self.assertEqual(self.fibonacci(0), 0)
        self.assertEqual(self.fibonacci(1), 1)
        self.assertEqual(self.fibonacci(2), 1)
        self.assertEqual(self.fibonacci(3), 2)
        self.assertEqual(self.fibonacci(4), 3)
        self.assertEqual(self.fibonacci(5), 5)
        self.assertEqual(self.fibonacci(6), 8)
        self.assertEqual(self.fibonacci(7), 13)
        self.assertEqual(self.fibonacci(8), 21)
        self.assertEqual(self.fibonacci(9), 34)

    def test_fibonacci_input_negative_int(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)

    def test_fibonacci_input_float(self):
        with self.assertRaises(ValueError):
            self.fibonacci(2.5)

    def test_fibonacci_input_str(self):
        with self.assertRaises(ValueError):
            self.fibonacci("123")

    def test_fibonacci_input_none(self):
        with self.assertRaises(ValueError):
            self.fibonacci(None)

    def test_fibonacci_without_input(self):
        with self.assertRaises(TypeError):
            self.fibonacci()

    def test_fibonacci_input_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            self.fibonacci(15, 20)

    def test_fibonacci_caching_mechanism(self):
        self.fibonacci(5)
        self.fibonacci(8)
        self.fibonacci(4)
        self.assertEqual(self.fibonacci.cache, [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_fibonacci_cache_exists(self):
        self.assertEqual(self.fibonacci.cache, [0, 1])

    def test_fibonacci_instance_reusability(self):
        fibonacci2 = Fibonacci()
        fibonacci2(5)
        fibonacci2(6)
        self.assertNotEqual(self.fibonacci.cache, fibonacci2.cache)
