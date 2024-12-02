import unittest
from datetime import datetime
from unittest.mock import MagicMock
from src.business_day_counter import BusinessDayCounter


class TestBusinessDayCounter(unittest.TestCase):

    def setUp(self):
        # Setup mock object
        self.mock_day_utils_obj = MagicMock()

    def test_get_total_days(self):
        # Mock the method
        self.mock_day_utils_obj.days_count_between_dates.return_value = 1
        business_day_counter = BusinessDayCounter(day_utils_obj=self.mock_day_utils_obj)

        start_date = datetime(2013, 10, 7)
        end_date = datetime(2013, 10, 9)
        total_days = 0

        # Call the method
        result = business_day_counter.get_total_days(start_date, end_date, total_days)

        # Assert the return value
        self.assertEqual(result, 1)  # 9 - 7 days difference must be 1
        self.mock_day_utils_obj.days_count_between_dates.assert_called_once_with(
            start_date=start_date, end_date=end_date
        )

    def test_get_holidays_case_1(self):
        # Mock the method
        self.mock_day_utils_obj.calculate_public_holidays.return_value = 0
        business_day_counter = BusinessDayCounter(day_utils_obj=self.mock_day_utils_obj)

        # Inputs for the test case
        public_holiday_list = [
            datetime(2013, 12, 25),
            datetime(2013, 12, 26),
            datetime(2014, 1, 1),
        ]
        start_date = datetime(2013, 10, 7)
        end_date = datetime(2013, 10, 9)
        public_holidays = 0

        # Call the method
        result = business_day_counter.get_holidays(
            start_date, end_date, public_holidays, public_holiday_list
        )

        # Assert the result
        self.assertEqual(result, 0)  # No holidays in the given range
        self.mock_day_utils_obj.calculate_public_holidays.assert_called_once_with(
            start_date=start_date, end_date=end_date, public_holiday_list=public_holiday_list
        )

    def test_get_holidays_case_2(self):
        # Mock the method
        self.mock_day_utils_obj.calculate_public_holidays.return_value = 2
        business_day_counter = BusinessDayCounter(day_utils_obj=self.mock_day_utils_obj)

        # Inputs for the test case
        public_holiday_list = [
            datetime(2013, 12, 25),
            datetime(2013, 12, 26),
            datetime(2014, 1, 1),
        ]
        start_date = datetime(2013, 12, 24)
        end_date = datetime(2013, 12, 28)
        public_holidays = 0

        # Call the method
        result = business_day_counter.get_holidays(
            start_date, end_date, public_holidays, public_holiday_list
        )

        # Assert the result
        self.assertEqual(result, 2)  # 2 public holidays between 24th and 28th Dec
        self.mock_day_utils_obj.calculate_public_holidays.assert_called_once_with(
            start_date=start_date, end_date=end_date, public_holiday_list=public_holiday_list
        )

    def test_get_holidays_case_3(self):
        # Mock the method
        self.mock_day_utils_obj.calculate_public_holidays.return_value = 4
        business_day_counter = BusinessDayCounter(day_utils_obj=self.mock_day_utils_obj)

        # Inputs for the test case
        public_holiday_list = [
            datetime(2013, 12, 25),
            datetime(2013, 12, 26),
            datetime(2014, 1, 1),
        ]
        start_date = datetime(2013, 12, 24)
        end_date = datetime(2014, 1, 2)
        public_holidays = 0

        # Call the method
        result = business_day_counter.get_holidays(
            start_date, end_date, public_holidays, public_holiday_list
        )

        # Assert the result
        self.assertEqual(result, 4)  # 4 public holidays between 24th Dec and 2nd Jan
        self.mock_day_utils_obj.calculate_public_holidays.assert_called_once_with(
            start_date=start_date, end_date=end_date, public_holiday_list=public_holiday_list
        )


if __name__ == "__main__":
    unittest.main()
