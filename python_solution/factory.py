from abc import abstractmethod
from datetime import date, timedelta

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HolidayFactory(object):
    def __init__(self, start_date, end_date, holiday_rules):
        self.start_date = start_date
        self.end_date = end_date
        self.holiday_rules = holiday_rules
        self.possible_holidays = []

    @abstractmethod
    def get_obj(self):
        """
        Abstract method that should be implemented in subclasses.
        Returns the holiday object if valid, else None.
        """
        pass

    def generate_holiday(self):
        """
        Generate holiday objects for each holiday rule, without filtering by date yet.
        :return: List of datetime holiday objects objects.
        """
        logger.info("Starting holiday generation process.")

        for holiday in self.holiday_rules:
            holiday_type = holiday.get('holiday_type')
            logger.info(f"Processing holiday: {holiday}")
            if holiday_type == "moveable_holiday":
                logger.info(f"Generating moveable holiday: {holiday}")
                holiday_objects = MoveableHolidayFactory(holiday, self.start_date, self.end_date).get_obj()
                if holiday_objects:
                    logger.info(f"Added {len(holiday_objects)} moveable holidays.")
                else:
                    logger.info(f"No moveable holidays.")
            elif holiday_type == "certain_occurrence_holiday":
                logger.info(f"Generating certain occurrence holiday: {holiday}")
                holiday_objects = CertainOccurrenceHolidayFactory(holiday, self.start_date, self.end_date).get_obj()
                if holiday_objects:
                    logger.info(f"Added {len(holiday_objects)} certain occurrence holidays.")
                else:
                    logger.info(f"No certain occurrence holidays.")
            elif holiday_type == "public_holiday":
                logger.info(f"Generating public holiday: {holiday}")
                holiday_objects = PublicHolidayFactory(holiday, self.start_date, self.end_date).get_obj()
                if holiday_objects:
                    logger.info(f"Added {len(holiday_objects)} public holidays.")
                else:
                    logger.info(f"No public holidays.")
            else:
                logger.error(f"Holiday type '{holiday_type}' not supported.")
                raise Exception(f"Holiday type '{holiday_type}' not supported")
            self.possible_holidays.extend(holiday_objects)
        holidays = self.check_dates_in_range(self.possible_holidays)
        logger.info(f"Holiday generation process completed. Total holidays generated: {len(holidays)}")

        return holidays

    def filter_valid_holidays(self, holiday_date):
        """
        After generating holiday objects, filter those that are within the date range.
        :param holiday_date: Date object to be checked if it's within the date range.
        :return: Boolean value indicating if the holiday_date is within the range.
        """
        return self.start_date <= holiday_date <= self.end_date if holiday_date else False


    def generate_dates(self, *args, **kwargs):
        """
          Generate a list of holiday dates for the given holiday rule within the specified date range.

          This method calculates all possible holiday dates for a specific holiday rule, considering the
          gap in years between the start and end dates. It then filters out those holidays that do not fall
          within the valid range using the `filter_valid_holidays` method.

          :return: List of valid holiday dates within the range.
          :rtype: list[datetime.date]
          """
        generated_dates = []
        years_gap = self.end_date.year - self.start_date.year
        month, day = kwargs.get('month'), kwargs.get('day')
        # Iterate through each year within the gap and calculate the holiday date for each year
        if not month or not day:
            raise Exception("Month and day arguments are required.")

        for start_year in range(0, years_gap + 1):
            holiday_date = date(self.start_date.year + start_year, month, day)
            generated_dates.append(holiday_date)
        return generated_dates

    def check_dates_in_range(self, possible_holidays):
        """
        Filter the list of possible holidays to include only those within the valid date range.

        :param possible_holidays: List of dates to filter.
        :return: List of dates within the specified date range.
        """
        valid_holidays = []
        logger.info(f"Starting to check dates in range from {self.start_date} to {self.end_date}.")
        logger.info(f"Total possible holidays to check: {len(possible_holidays)}")

        for p_holiday in possible_holidays:
            if self.filter_valid_holidays(p_holiday):
                logger.info(f"Date {p_holiday} is within range.")
                valid_holidays.append(p_holiday)
            else:
                logger.warning(f"Date {p_holiday} is out of range.")

        logger.info(f"Finished filtering. Total valid holidays: {len(valid_holidays)}")
        return valid_holidays


class PublicHolidayFactory(HolidayFactory):
    def __init__(self, holiday, start_date, end_date):
        super().__init__(start_date, end_date, holiday)
        self.holiday = holiday

    def get_obj(self):
        return self.generate_dates(**self.holiday)

class MoveableHolidayFactory(HolidayFactory):
    def __init__(self, holiday, start_date, end_date):
        super().__init__(start_date, end_date, holiday)
        self.holiday = holiday

    def move_date(self, date):
        """
          Adjusts a holiday date if it falls on a weekend (Saturday or Sunday).
          If the holiday falls on:
          - Saturday, move it to Monday.
          - Sunday, move it to Monday.

          :param date: A date object representing the holiday to be adjusted.
          :return: Adjusted date (if holiday falls on weekend).
          """
        original_date = date
        if date.weekday() == 5:  # Saturday
            date += timedelta(days=2)  # Move to Monday
            logging.info(f"Holiday {original_date} is a Saturday. Moved to Monday: {date}")
        elif date.weekday() == 6:  # Sunday
            date += timedelta(days=1)  # Move to Monday
            logging.info(f"Holiday {original_date} is a Sunday. Moved to Monday: {date}")
        return date

    def get_obj(self):
        """
        Logic for moveable holiday (e.g., New Years).
        You'd need to implement how to calculate these holidays (e.g., New Years). Before calculate the dates, it's need
        to be pre-process
        :return: List of Date object.
        """

        possible_holidays = self.generate_dates(**self.holiday)
        moved_dates = [self.move_date(moveable_holiday) for moveable_holiday in possible_holidays]
        return moved_dates

class CertainOccurrenceHolidayFactory(HolidayFactory):
    def __init__(self, holiday, start_date, end_date):
        super().__init__(start_date, end_date, holiday)
        self.holiday = holiday

    def get_obj(self):
        """
        Logic for certain occurrence holidays (e.g., second Monday in October).
        You need to implement the logic for calculating these holidays.
        :return: Date object or None.
        """
        # Example: Getting the second Monday in October
        return self.generate_dates(**self.holiday)

    #Ovveride
    def generate_dates(self, *args, **kwargs):
        """
        Get the nth weekday (e.g., 2nd Monday) in a given month.
        :param month: Month as integer (1=January, 12=December).
        :param weekday: Weekday as integer (0=Monday, 6=Sunday).
        :param occurrence: The occurrence (1=first, 2=second, etc.)
        :return: Date object for the nth weekday of the month.
        """
        years_gap = self.end_date.year - self.start_date.year
        month, weekday, occurrence = kwargs.get('month'), kwargs.get('day'), kwargs.get('occurrence')

        if not month and not weekday and occurrence:
            raise Exception("Month, Weekday and Occurrence required")

        possible_holidays = []
        for start_year in range(0, years_gap + 1):
            first_day_of_month = date(self.start_date.year + start_year , month, 1)
            first_weekday_of_month = first_day_of_month.weekday()

            # Calculate the day of the month for the nth weekday
            day_offset = (weekday - first_weekday_of_month) % 7
            nth_weekday_date = first_day_of_month + timedelta(days=day_offset + (occurrence - 1) * 7)
            possible_holidays.append(nth_weekday_date)
        return possible_holidays


