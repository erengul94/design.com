import logging

from src.validator import validate_dates
from datetime import date
from datetime import timedelta

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

NUMBER_OF_DAYS_IN_A_WEEK = 7
WEEK_DAYS_RANGE = {0, 1, 2, 3, 4}  # Monday, Tuesday... Friday
WEEKEND_DAYS_RANGE = {5, 6}

class DayUtils:
    def __init__(self):
        pass

    @staticmethod
    @validate_dates
    def days_count_between_dates(start_date, end_date):
        """
        Calculates the number of full days between two dates.

        This method computes the difference in days between the `end_date` and the `start_date`.
        It subtracts 1 from the result to exclude the start date itself from the count.
        For example:
        - If `start_date` is 2024-01-01 and `end_date` is 2024-01-05,
          the difference would normally be 4 days, but the method returns 3
          because the first day is excluded.

        Precondition:
        - The `validate_dates` custom annotation ensures that both `start_date` and `end_date`
          are valid datetime objects, and `end_date` is not earlier than `start_date`.

        :param start_date: A datetime.date object representing the start date.
        :param end_date: A datetime.date object representing the end date.
        :return: An integer representing the number of full days between the two dates.
        """
        return (end_date - start_date).days -1

    @staticmethod
    def remainder(total_days):
        """
        Calculates the remainder when dividing the total number of days by the number of days in a week (7).

        :param total_days: int -> Total days between two dates
        :return: int -> Remainder of the division
        """
        logger.info("Calculating remainder for total_days_count_between_dates: %d", total_days)

        remainder_value = total_days % NUMBER_OF_DAYS_IN_A_WEEK
        logger.info("Remainder calculated: %d", remainder_value)

        return remainder_value

    @staticmethod
    def quotient(total_days):
        """
        Calculates the quotient when dividing the total number of days by the number of days in a week (7).
        This value represents the number of full weeks within the given date range.

        :param total_days: int -> Total days between two dates
        :return: int -> Quotient (number of full weeks)
        """
        logger.info("Calculating quotient for total_days_count_between_dates: %d", total_days)

        quotient_value = total_days // NUMBER_OF_DAYS_IN_A_WEEK
        logger.info("Quotient calculated: %d", quotient_value)

        return quotient_value


    def total_weekend_days_count(self, start_date, total_days):
        """
        Calculates the total number of weekend days (Saturdays and Sundays) within a given date range.

        :param start_date: datetime.date -> The start date of the range
        :param total_days: int -> The total number of days between the two dates
        :return: int -> The total number of weekend days (Saturdays and Sundays) in the range
        """
        logger.info("Calculating weekend days between %s and total days count: %d", start_date, total_days)

        remaining_weekend_days = 0
        remainder = self.remainder(total_days)
        quotient = self.quotient(total_days)

        logger.info("Remainder count: %d, Quotient count: %d", remainder, quotient)

        start_date_index = start_date.weekday()

        if remainder > 0:
            remaining_weekend_days += self.remaining_weekend_days_count(start_date_index, remainder, remaining_weekend_days)

        total_weekend_days = quotient * 2 + remaining_weekend_days
        logger.info("Total weekend days: %d", total_weekend_days)
        return total_weekend_days

    @staticmethod
    def remaining_weekend_days_count(start_date_index, remainder, remaining_weekend_days):
        """
        Calculates the number of weekend days (Saturdays and Sundays) in the remaining days
        after full weeks have been considered.

        :param start_date_index: int -> The weekday index of the start date (0 = Monday, 6 = Sunday)
        :param remainder: int -> The number of days remaining after full weeks
        :param remaining_weekend_days: int -> reference to keep value

        :return: int -> The count of weekend days (Saturdays and Sundays)
        """
        logger.info("Calculating remaining weekend days from start index: %d for remainder: %d days", start_date_index, remainder)

        for i in range(1, remainder + 1):
            current_day = (start_date_index + i) % 7 # 6 + 0 =6 still in sunday
            if current_day in {5, 6}:  # Saturday (5) or Sunday (6)
                remaining_weekend_days += 1
                logger.info("Remaining weekend day detected on day %d (Index: %d)", i + 1, current_day)

        logger.info("Total remaining weekend days: %d", remaining_weekend_days)
        return remaining_weekend_days


    @staticmethod
    def calculate_public_holidays(start_date, end_date, public_holiday_list):
        """
        Calculate the total number of public holidays within the given date range.

        This method takes a list of pre-generated public holidays and filters them
        to identify which holidays fall between the specified start and end dates.

        :param start_date: The start date of the range.
        :param end_date: The end date of the range.
        :param public_holiday_list: List of all possible public holidays.
        :return: Number of public holidays within the range.
        :rtype: int
        """
        logging.info(f"Filtering public holidays from the generated list.")
        public_holiday_days_total_count = 0

        for holiday in public_holiday_list:
            if (holiday.weekday() in WEEK_DAYS_RANGE) and (start_date < holiday < end_date):
                public_holiday_days_total_count += 1

        return public_holiday_days_total_count


    @staticmethod
    def filter_date(start_date, original_date, end_date):
        """
        Filters a date based on whether it falls within a specified date range.

        :param start_date: The start date of the range.
        :param original_date: The date to check if it falls within the range.
        :param end_date: The end date of the range.

        :return: bool - True if the original date is within the range, False otherwise. Returns False if the original date is None.
        """
        return start_date <= original_date <= end_date if original_date else False

    @staticmethod
    def generates_dates_frequency_for_certain_period(start_date, period, month, day):
        """
        Generates a list of dates occurring on a specific month and day for a given number of years, starting from a given date.

        :param start_date: The starting date to base the year calculation on.
        :param period: The number of years after the start date to generate possible dates.
        :param month: The month (as an integer) of the desired date.
        :param day: The day (as an integer) of the desired date.

        :return: list - A list of `date` objects representing the possible holiday dates.
        """
        possible_dates = []
        for start_year in range(0, period + 1):
            holiday_date = date(start_date.year + start_year, month, day)
            possible_dates.append(holiday_date)
        return possible_dates

    @staticmethod
    def generates_occurrence_dates_frequency_for_certain_period(start_date, period, month, day, occurrence):
        """
            Generates a list of dates occurring on a specific month and day for a given number of years, starting from a given date.

            :param start_date: The starting date to base the year calculation on.
            :param period: The number of years after the start date to generate possible dates.
            :param month: The month (as an integer) of the desired date.
            :param day: The day (as an integer) of the desired date.
            :param occurrence: The occurrence number (e.g., 1st, 2nd, etc.)

            :return: list - A list of `date` objects representing the possible holiday dates.
            """
        possible_holidays = []
        for start_year in range(0, period + 1):
            first_day_of_month = date(start_date.year + start_year, month, 1)
            first_weekday_of_month = first_day_of_month.weekday()

            day_offset = (day - first_weekday_of_month) % 7
            nth_weekday_date = first_day_of_month + timedelta(days=day_offset + (occurrence - 1) * 7)
            possible_holidays.append(nth_weekday_date)
        return possible_holidays