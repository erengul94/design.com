import unittest
import datetime
from datetime import date
from src.validator import validate_dates

class TestValidateDatesDecorator(unittest.TestCase):
    """
    Unit test class to test the behavior of the validate_dates decorator.
    This tests different scenarios like valid dates, invalid date types,
    invalid calendar dates, and invalid date ranges (start_date > end_date).
    """

    def setUp(self):
        """
        Setup method to initialize the sample decorated function for testing.
        This function calculates the difference in days between two dates.
        The validate_dates decorator is applied to this function for testing.
        """
        @validate_dates
        def sample_function(start_date, end_date):
            return (end_date - start_date).days

        self.decorated_function = sample_function

    def test_valid_dates(self):
        """
        Test case for valid date range where start_date is earlier than end_date.
        This checks that the function correctly calculates the difference in days.
        """
        start_date = date(2023, 1, 1)
        end_date = date(2023, 1, 10)

        result = self.decorated_function(start_date, end_date)
        self.assertEqual(result, 9)  # 10 - 1 = 9 days difference

    def test_invalid_date_types(self):
        """
        Test case for invalid date types where the input is not of type datetime.date.
        This checks that a ValueError is raised with the appropriate error message.
        """
        with self.assertRaises(ValueError) as context:
            self.decorated_function("2023-01-01", "2023-01-10")
        self.assertEqual(str(context.exception), "Both start_date and end_date must be of type datetime.date")

    def test_invalid_calendar_date(self):
        """
        Test case for an invalid calendar date where February 29 is used in a non-leap year.
        This checks that a ValueError is raised when an invalid calendar date is passed.
        """
        with self.assertRaises(ValueError) as context:
            self.decorated_function(datetime.date(2023, 2, 29), datetime.date(2023, 3, 1))  # Feb 29 is not valid in 2023
        self.assertEqual(str(context.exception), "day is out of range for month")

    def test_start_date_greater_than_end_date(self):
        """
        Test case where the start_date is later than the end_date.
        This checks that the function returns 0 for an invalid date range.
        """
        start_date = date(2023, 1, 10)
        end_date = date(2023, 1, 1)

        result = self.decorated_function(start_date, end_date)
        self.assertEqual(result, 0)  # Returns 0 for invalid date range

    def test_start_date_equal_to_end_date(self):
        """
        Test case where the start_date is equal to the end_date.
        This checks that the function returns 0 for an invalid date range.
        """
        start_date = date(2023, 1, 10)
        end_date = date(2023, 1, 10)

        result = self.decorated_function(start_date, end_date)
        self.assertEqual(result, 0)  # Returns 0 for invalid date range


if __name__ == "__main__":
    unittest.main()
