import logging

from annotations import validate_dates
from factory import HolidayFactory
from holiday_counter import PublicHolidayCounter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

NUMBER_OF_DAYS_IN_A_WEEK = 7

class DayCalculator:
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
    def remainder(total_days_count_between_dates):
        """
        Calculates the remainder when dividing the total number of days by the number of days in a week (7).

        :param total_days_count_between_dates: int -> Total days between two dates
        :return: int -> Remainder of the division
        """
        logger.info("Calculating remainder for total_days_count_between_dates: %d", total_days_count_between_dates)

        remainder_value = total_days_count_between_dates % NUMBER_OF_DAYS_IN_A_WEEK
        logger.info("Remainder calculated: %d", remainder_value)

        return remainder_value

    @staticmethod
    def quotient(total_days_count_between_dates):
        """
        Calculates the quotient when dividing the total number of days by the number of days in a week (7).
        This value represents the number of full weeks within the given date range.

        :param total_days_count_between_dates: int -> Total days between two dates
        :return: int -> Quotient (number of full weeks)
        """
        logger.info("Calculating quotient for total_days_count_between_dates: %d", total_days_count_between_dates)

        quotient_value = total_days_count_between_dates // NUMBER_OF_DAYS_IN_A_WEEK
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
            remaining_weekend_days += self.remaining_weekend_days_count(start_date_index, remainder)

        total_weekend_days = quotient * 2 + remaining_weekend_days
        logger.info("Total weekend days: %d", total_weekend_days)
        return total_weekend_days

    @staticmethod
    def remaining_weekend_days_count(start_date_index, remainder):
        """
        Calculates the number of weekend days (Saturdays and Sundays) in the remaining days
        after full weeks have been considered.

        :param start_date_index: int -> The weekday index of the start date (0 = Monday, 6 = Sunday)
        :param remainder: int -> The number of days remaining after full weeks
        :return: int -> The count of weekend days (Saturdays and Sundays)
        """
        logger.info("Calculating remaining weekend days from start index: %d for remainder: %d days", start_date_index, remainder)

        remaining_weekend_days = 0

        for i in range(1, remainder + 1):
            current_day = (start_date_index + i) % 7 # 6 + 0 =6 still in sunday
            if current_day in {5, 6}:  # Saturday (5) or Sunday (6)
                remaining_weekend_days += 1
                logger.info("Remaining weekend day detected on day %d (Index: %d)", i + 1, current_day)

        logger.info("Total remaining weekend days: %d", remaining_weekend_days)
        return remaining_weekend_days

    def calculate_public_holidays_with_rules(self, start_date, end_date, holiday_rules):
        """
        Calculate the total number of public holidays in the range.

        :param start_date: The start date of the range.
        :param end_date: The end date of the range.
        :param holiday_rules: Rules defining the holidays.
        :return: Total number of public holidays.
        """
        logging.info(f"Generating holidays using rules: {holiday_rules}")
        holiday_factory = HolidayFactory(start_date=start_date, end_date=end_date, holiday_rules=holiday_rules)
        public_holiday_list = holiday_factory.generate_holiday()
        public_holidays = self.calculate_public_holidays(start_date, end_date, public_holiday_list)
        logging.info(f"Total public holidays between {start_date} and {end_date}: {public_holidays}")
        return public_holidays


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
        public_holidays = PublicHolidayCounter(
            start_date=start_date, end_date=end_date, public_holiday_list=public_holiday_list
        ).get_holiday_date()

        return public_holidays