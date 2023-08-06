import numpy as np
from statistics import mode


class Statistics:
    def __init__(self, *nums):
        if len(nums) == 0:
            raise ValueError("At least one number must be provided.")
        self.nums = np.array(nums)

    def mean(self):
        """Calculate the mean (average) of the numbers."""
        return np.mean(self.nums)

    def median(self):
        """Calculate the median of the numbers."""
        return np.median(self.nums)

    def mode(self):
        """Find the mode of the numbers."""
        return mode(self.nums)

    def standard_deviation(self):
        """Calculate the sample standard deviation of the numbers."""
        return np.std(self.nums, ddof=1)

    def variance(self):
        """Calculate the sample variance of the numbers."""
        return np.var(self.nums, ddof=1)

    def percentile_and_quartile(self, q):
        """Calculate the specified percentile or quartile of the numbers."""
        return np.percentile(self.nums, q)

    def correlation(self, value1, value2):
        """Calculate the correlation coefficient between two lists of numbers."""
        if len(value1) != len(value2):
            raise ValueError("Both lists must have the same length.")
        return np.corrcoef(value1, value2)[0, 1]

    def covariance(self, value1, value2):
        """Calculate the covariance between two lists of numbers."""
        if len(value1) != len(value2):
            raise ValueError("Both lists must have the same length.")
        return np.cov(value1, value2, ddof=1)[0, 1]
