import unittest
import logging
from datetime import datetime
from src.business_day_counter import BusinessDayCounter
from unittest.mock import MagicMock

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class TestTask1(unittest.TestCase):
    """
    Unit tests for the BusinessDayCounter class.
    """

    def setUp(self):
        """
        Set up mock objects and test data before each test.
        """
        logging.info("Setting up mock objects for BusinessDayCounter...")
        self.mock_day_utils_obj = MagicMock()
        self.business_day_counter = BusinessDayCounter(day_utils_obj=self.mock_day_utils_obj)

    def test_task1_case1(self):
        """
        Test weekdays calculation for 7th October to 9th October 2013 (1 weekday).
        """
        logging.info("Running test_task1_case1...")
        start_date = datetime(2013, 10, 7)
        end_date = datetime(2013, 10, 9)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=1)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=0)

        weekdays = self.business_day_counter.weekdays_between_two_dates(start_date, end_date)
        logging.info(f"Weekdays calculated: {weekdays}")
        self.assertEqual(weekdays, 1)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=1
        )

    def test_task1_case2(self):
        """
        Test weekdays calculation for 5th October to 14th October 2013 (5 weekdays).
        """
        logging.info("Running test_task1_case2...")
        start_date = datetime(2013, 10, 5)
        end_date = datetime(2013, 10, 14)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=8)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=3)

        weekdays = self.business_day_counter.weekdays_between_two_dates(start_date, end_date)
        logging.info(f"Weekdays calculated: {weekdays}")
        self.assertEqual(weekdays, 5)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=8
        )

    def test_task1_case3(self):
        """
        Test weekdays calculation for 7th October 2013 to 1st January 2014 (61 weekdays).
        """
        logging.info("Running test_task1_case3...")
        start_date = datetime(2013, 10, 7)
        end_date = datetime(2014, 1, 1)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=85)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=24)

        weekdays = self.business_day_counter.weekdays_between_two_dates(start_date, end_date)
        logging.info(f"Weekdays calculated: {weekdays}")
        self.assertEqual(weekdays, 61)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=85
        )

    def test_task1_case4(self):
        """
        Test weekdays calculation for a case with no valid days (7th October 2013 to 5th October 2023).
        """
        logging.info("Running test_task1_case4...")
        start_date = datetime(2013, 10, 7)
        end_date = datetime(2023, 10, 5)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=0)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=0)

        weekdays = self.business_day_counter.weekdays_between_two_dates(start_date, end_date)
        logging.info(f"Weekdays calculated: {weekdays}")
        self.assertEqual(weekdays, 0)


if __name__ == "__main__":
    logging.info("Starting TestBusinessDayCounter tests...")
    unittest.main()
