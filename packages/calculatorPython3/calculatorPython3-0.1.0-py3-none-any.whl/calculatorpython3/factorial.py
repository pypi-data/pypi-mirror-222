import math


class Combinatorics:
    @staticmethod
    def factorial(n):
        """Calculate the factorial of a number."""
        return math.factorial(n)

    @staticmethod
    def nCr(n, r):
        """Calculate the number of combinations (n choose r)."""
        if 0 <= r <= n:
            return math.comb(n, r)
        else:
            raise ValueError(
                "Invalid values for n and r. r should be between 0 and n.")

    @staticmethod
    def nPr(n, r):
        """Calculate the number of permutations (n permute r)."""
        if 0 <= r <= n:
            return math.perm(n, r)
        else:
            raise ValueError(
                "Invalid values for n and r. r should be between 0 and n.")
