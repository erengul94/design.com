import unittest
import logging
from datetime import datetime
from src.business_day_counter import BusinessDayCounter
from unittest.mock import MagicMock

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class TestTask3(unittest.TestCase):
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
        self.holiday_rules = [
            {"holiday_type": "public_holiday",
             "description": "Anzac Day",
             "month": 4,
             "day": 25
             },
            {
                "holiday_type": "moveable_holiday",
                "description": "New Year's Day",
                "month": 1,
                "day": 1},
            {
                "holiday_type": "certain_occurrence_holiday",
                "description": "Queen's Birthday",
                "month": 6,
                "day": 0,
                "occurrence": 2
            }
        ]

    def test_task3_case1(self):
        """
        Test the calculation of weekdays between two dates (7th to 9th October 2013).
        """
        logging.info("Running test_task3_case1...")
        start_date = datetime(2013, 10, 7)
        end_date = datetime(2013, 10, 9)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=1)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=0)
        self.business_day_counter.get_holidays = MagicMock(return_value=0)

        weekdays = self.business_day_counter.business_days_between_two_dates(
            start_date, end_date, holiday_rules=self.holiday_rules
        )

        logging.info(f"Weekdays calculated: {weekdays}")
        self.assertEqual(weekdays, 1)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=1
        )

    def test_task3_case2(self):
        """
        It's test new years, in 2023, it should move the monday!. So testing will between
        26th of December 2022 - 4th of January 2023
        """
        logging.info("Running test_task3_case2...")
        start_date = datetime(2022, 12, 26)
        end_date = datetime(2023, 1, 4)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=8)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=2)
        self.business_day_counter.get_holidays = MagicMock(return_value=1)

        workdays = self.business_day_counter.business_days_between_two_dates(
            start_date, end_date, holiday_rules=self.holiday_rules
        )

        logging.info(f"Business calculated: {workdays}")
        self.assertEqual(workdays, 5)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=8
        )

    def test_task3_case2(self):
        """
        It's test Anzac Days, in 2023,  So testing will between
        17th of April 2022 - 27th of April 2023
        """
        logging.info("Running test_task3_case3...")
        start_date = datetime(2023, 4, 17)
        end_date = datetime(2023, 4, 27)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=9)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=2)
        self.business_day_counter.get_holidays = MagicMock(return_value=1)

        workdays = self.business_day_counter.business_days_between_two_dates(
            start_date, end_date, holiday_rules=self.holiday_rules
        )

        logging.info(f"Business calculated: {workdays}")
        self.assertEqual(workdays, 6)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=9
        )

    def test_task3_case3(self):
        """
        It's test Queen's Birthday Days, in 2023,  So testing will between
        5th of June 2023 - 14th of June 2023
        """
        logging.info("Running test_task2_case2...")
        start_date = datetime(2023, 6, 5)
        end_date = datetime(2023, 6, 14)

        # Mock method return values
        self.business_day_counter.get_total_days = MagicMock(return_value=8)
        self.mock_day_utils_obj.total_weekend_days_count = MagicMock(return_value=2)
        self.business_day_counter.get_holidays = MagicMock(return_value=1)

        workdays = self.business_day_counter.business_days_between_two_dates(
            start_date, end_date, holiday_rules=self.holiday_rules
        )

        logging.info(f"Business calculated: {workdays}")
        self.assertEqual(workdays, 5)

        # Verify the calls
        self.business_day_counter.get_total_days.assert_called_once_with(
            start_date=start_date, end_date=end_date, total_days=0
        )
        self.mock_day_utils_obj.total_weekend_days_count.assert_called_once_with(
            start_date=start_date, total_days=8
        )

if __name__ == "__main__":
    logging.info("Starting tests...")
    unittest.main()
