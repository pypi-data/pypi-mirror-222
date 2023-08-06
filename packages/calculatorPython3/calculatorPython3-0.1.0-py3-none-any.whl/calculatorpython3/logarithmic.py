import numpy as np
import math as m


class Logarithmic:
    def __init__(self, value):
        self.value = value

    def log(self):
        """Calculate the natural logarithm (base e) of the value."""
        if self.value <= 0:
            raise ValueError(
                "The value must be greater than zero for logarithmic calculations.")
        return np.log(self.value)

    def log_base(self, base=m.e):
        """Calculate the logarithm of the value with the specified base (default is natural logarithm)."""
        if self.value <= 0 or base <= 0:
            raise ValueError(
                "Both the value and the base must be greater than zero for logarithmic calculations.")
        return m.log(self.value, base)

    def log2(self):
        """Calculate the base-2 logarithm of the value."""
        if self.value <= 0:
            raise ValueError(
                "The value must be greater than zero for logarithmic calculations.")
        return np.log2(self.value)

    def log10(self):
        """Calculate the base-10 logarithm of the value."""
        if self.value <= 0:
            raise ValueError(
                "The value must be greater than zero for logarithmic calculations.")
        return np.log10(self.value)

    def log1p(self, base=m.e):
        """Calculate the logarithm of the value plus one with the specified base (default is natural logarithm)."""
        if self.value <= -1 or base <= 0:
            raise ValueError(
                "The value must be greater than or equal to -1 and the base must be greater than zero for log1p calculations.")
        return np.log1p(self.value + base)
