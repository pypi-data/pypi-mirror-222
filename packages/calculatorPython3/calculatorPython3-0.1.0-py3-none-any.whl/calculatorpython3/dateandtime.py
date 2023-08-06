import datetime
from dateutil.relativedelta import relativedelta


class DateandTimeCalculations:
    def __init__(self, date):
        if not isinstance(date, datetime.datetime):
            raise ValueError(
                "The 'date' parameter must be a valid datetime object.")
        self.date = date

    def add_days(self, days):
        """Add the specified number of days to the date."""
        return self.date + datetime.timedelta(days=days)

    def subtract_days(self, days):
        """Subtract the specified number of days from the date."""
        return self.date - datetime.timedelta(days=days)

    def add_months(self, months):
        """Add the specified number of months to the date."""
        return self.date + relativedelta(months=months)

    def subtract_months(self, months):
        """Subtract the specified number of months from the date."""
        return self.date - relativedelta(months=months)

    def add_years(self, years):
        """Add the specified number of years to the date."""
        try:
            return self.date.replace(year=self.date.year + years)
        except ValueError:
            # Handle non-leap years (e.g., February 29)
            if self.date.month == 2 and self.date.day == 29:
                return self.date.replace(year=self.date.year + years, month=2, day=28)
            raise

    def subtract_years(self, years):
        """Subtract the specified number of years from the date."""
        return self.date - relativedelta(years=years)

    @staticmethod
    def date_difference(start_date, end_date):
        """Calculate the number of days between two dates."""
        if not isinstance(start_date, datetime.datetime) or not isinstance(end_date, datetime.datetime):
            raise ValueError(
                "Both start_date and end_date must be valid datetime objects.")
        return (end_date - start_date).days

    @staticmethod
    def format_date(date, format_string="%Y-%m-%d"):
        """Format the given date according to the specified format."""
        if not isinstance(date, datetime.datetime):
            raise ValueError(
                "The 'date' parameter must be a valid datetime object.")
        return date.strftime(format_string)
