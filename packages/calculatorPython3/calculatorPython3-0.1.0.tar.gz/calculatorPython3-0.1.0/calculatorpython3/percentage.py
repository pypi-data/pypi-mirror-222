class Percentage:
    def __init__(self, value):
        self.value = value

    def percentage_of(self, percent):
        """Calculate the percentage of the value."""
        return (percent / 100) * self.value

    def percentage_change(self, old_value, direction='any'):
        """Calculate the percentage change between the current value and the old value."""
        if direction == 'any':
            direction = 'increase' if self.value >= old_value else 'decrease'
        elif direction not in ('increase', 'decrease'):
            raise ValueError(
                "Invalid value for 'direction'. Use 'increase' or 'decrease'.")

        change = self.value - old_value
        if direction == 'increase':
            return (change / abs(old_value)) * 100
        else:
            return (-change / abs(old_value)) * 100

    def percentage_difference(self, other_value):
        """Calculate the percentage difference between the current value and another value."""
        return ((other_value - self.value) / abs(self.value)) * 100

    def percentage_increase(self, increase):
        """Calculate the percentage increase from the current value by the specified increase."""
        return (increase / abs(self.value)) * 100

    def percentage_decrease(self, decrease):
        """Calculate the percentage decrease from the current value by the specified decrease."""
        return (-decrease / abs(self.value)) * 100
