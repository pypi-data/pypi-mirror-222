import numpy as np


class NormalCalculator:
    def __init__(self, *nums):
        self.nums = nums

    def addition(self):
        """Calculate the sum of all the numbers."""
        return sum(self.nums)

    def subtraction(self):
        """Calculate the result of subtracting all the numbers."""
        if len(self.nums) < 2:
            raise ValueError("Subtraction requires at least two numbers.")
        return self.nums[0] - sum(self.nums[1:])

    def multiplication(self):
        """Calculate the product of all the numbers."""
        return np.prod(self.nums)

    def division(self):
        """Calculate the result of dividing the numbers."""
        if len(self.nums) < 2:
            raise ValueError("Division requires at least two numbers.")
        return self.nums[0] / np.prod(self.nums[1:])

    def power(self, exponent):
        """Calculate the numbers raised to the given exponent."""
        return [num ** exponent for num in self.nums]

    def square_root(self):
        """Calculate the square root of the numbers."""
        return [np.sqrt(num) for num in self.nums]

    def apply_operation(self, operation):
        """Apply the given operation to all the numbers."""
        return [operation(num) for num in self.nums]

    def absolute_value(self):
        """Calculate the absolute value of the numbers."""
        return self.apply_operation(abs)

    def modulo(self):
        """Calculate the modulo of the two numbers."""
        if len(self.nums) != 2:
            raise ValueError("Modulo operation requires exactly two numbers.")
        return np.mod(*self.nums)

    @staticmethod
    def gcd(a, b):
        """Calculate the greatest common divisor (GCD) of two numbers."""
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        """Calculate the least common multiple (LCM) of two numbers."""
        return abs(a * b) // NormalCalculator.gcd(a, b)


class RoundingandPrecision:
    def __init__(self, value):
        self.value = value

    def round_to_integer(self):
        """Round the value to the nearest integer."""
        return int(round(self.value))

    def round_to_precision(self, precision):
        """Round the value to the specified precision."""
        return round(self.value, precision)
