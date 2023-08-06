import numpy as np
from math import degrees, radians


class Trigonometric:
    def __init__(self, value):
        self.value = value

    def sin(self, unit='radians'):
        """Calculate the sine of the value."""
        if unit == 'degrees':
            value_in_radians = radians(self.value)
            return np.sin(value_in_radians)
        elif unit == 'radians':
            return np.sin(self.value)
        else:
            raise ValueError("Invalid unit. Use 'degrees' or 'radians'.")

    def cos(self, unit='radians'):
        """Calculate the cosine of the value."""
        if unit == 'degrees':
            value_in_radians = radians(self.value)
            return np.cos(value_in_radians)
        elif unit == 'radians':
            return np.cos(self.value)
        else:
            raise ValueError("Invalid unit. Use 'degrees' or 'radians'.")

    def tan(self, unit='radians'):
        """Calculate the tangent of the value."""
        if unit == 'degrees':
            value_in_radians = radians(self.value)
            return np.tan(value_in_radians)
        elif unit == 'radians':
            return np.tan(self.value)
        else:
            raise ValueError("Invalid unit. Use 'degrees' or 'radians'.")

    def asin(self, unit='radians'):
        """Calculate the arcsine of the value."""
        result = np.arcsin(self.value)
        if unit == 'degrees':
            return degrees(result)
        elif unit == 'radians':
            return result
        else:
            raise ValueError("Invalid unit. Use 'degrees' or 'radians'.")

    def acos(self, unit='radians'):
        """Calculate the arccosine of the value."""
        result = np.arccos(self.value)
        if unit == 'degrees':
            return degrees(result)
        elif unit == 'radians':
            return result
        else:
            raise ValueError("Invalid unit. Use 'degrees' or 'radians'.")

    def atan(self, unit='radians'):
        """Calculate the arctangent of the value."""
        result = np.arctan(self.value)
        if unit == 'degrees':
            return degrees(result)
        elif unit == 'radians':
            return result
        else:
            raise ValueError("Invalid unit. Use 'degrees' or 'radians'.")

    def sinh(self):
        """Calculate the hyperbolic sine of the value."""
        return np.sinh(self.value)

    def cosh(self):
        """Calculate the hyperbolic cosine of the value."""
        return np.cosh(self.value)

    def tanh(self):
        """Calculate the hyperbolic tangent of the value."""
        return np.tanh(self.value)
