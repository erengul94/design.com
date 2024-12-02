import unittest
import logging
from datetime import datetime
from src.business_day_counter import BusinessDayCounter
from unittest.mock import MagicMock

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class TestTask2(unittest.TestCase):
    """
    Unit tests for the BusinessDayCounter class.
    """

    def setUp(self):
        """
        Set up mock objects and test data before each test.
        """
        logging.info("Setting up mock objects and test data...")
        # Setup mock object
        self.mock_day_utils_obj = MagicMock()
        self.business_day_counter = BusinessDayCounter(day_utils_obj=self.mock_day_utils_obj)

        # Public holidays
        self.first_public_holiday = datetime(2013, 12, 25)
        self.second_public_holiday = datetime(2013, 12, 26)
        self.third_public_holiday = datetime(2014, 1, 1)
        self.public_holiday_list = [self.first_public_holiday, self.second_public_holiday, self.third_public_holiday]

    def test_task2_case1(self):
        """
        Test the calculation of weekdays between two dates (7th to 9th October 2013).
        """
        logging.info("Running test_task2_case1...")
        start_date = datetime(2013, 10, 7)
        end_date = datetime(2013, 10, 9)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=1)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=0)
        self.business_day_counter.get_holidays = MagicMock(return_value=0)

        weekdays = self.business_day_counter.business_days_between_two_dates(
            start_date, end_date, public_holiday_list=self.public_holiday_list
        )

        logging.info(f"Business calculated: {weekdays}")
        self.assertEqual(weekdays, 1)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=1
        )

    def test_task2_case2(self):
        """
        Test the calculation of weekdays between two dates (24th to 30th December 2013) with holidays.
        """
        logging.info("Running test_task2_case2...")
        start_date = datetime(2013, 12, 22)
        end_date = datetime(2013, 12, 30)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=7)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=2)
        self.business_day_counter.get_holidays = MagicMock(return_value=2)

        weekdays = self.business_day_counter.business_days_between_two_dates(
            start_date, end_date, public_holiday_list=self.public_holiday_list
        )

        logging.info(f"Business calculated: {weekdays}")
        self.assertEqual(weekdays, 3)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=7
        )

    def test_task2_case3(self):
        """
        Test the calculation of weekdays between two dates (7th October 2013 to 1st January 2014).
        """
        logging.info("Running test_task2_case3...")
        start_date = datetime(2013, 10, 7)
        end_date = datetime(2014, 1, 1)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=85)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=24)
        self.business_day_counter.get_holidays = MagicMock(return_value=2)

        weekdays = self.business_day_counter.business_days_between_two_dates(
            start_date, end_date, public_holiday_list=self.public_holiday_list
        )

        logging.info(f"Business calculated: {weekdays}")
        self.assertEqual(weekdays, 59)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=85
        )


if __name__ == "__main__":
    logging.info("Starting tests...")
    unittest.main()
