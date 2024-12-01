from abc import abstractmethod, ABC
from datetime import timedelta
from src.date_utils import DayUtils
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HolidayFactory(object):
    def __init__(self, holiday_rules, start_date, end_date):
        self.holiday_rules = holiday_rules
        self.created_objects = []
        self.start_date = start_date
        self.end_date = end_date

    def get_objects(self):
        for holiday_rule in self.holiday_rules:

            holiday_type = holiday_rule.get("holiday_type")

            if holiday_type:

                if holiday_type == "moveable_holiday":
                    self.created_objects.append(MoveableHoliday(holiday_rule=holiday_rule,
                                                                start_date=self.start_date,
                                                                end_date=self.end_date))

                elif holiday_type == "public_holiday":
                    self.created_objects.append(PublicHoliday(holiday_rule=holiday_rule,
                                                                start_date=self.start_date,
                                                                end_date=self.end_date))

                elif holiday_type == "certain_occurrence_holiday":
                    self.created_objects.append(CertainOccurrenceHoliday(holiday_rule=holiday_rule,
                                                                         start_date=self.start_date,
                                                                         end_date=self.end_date))

                else:
                    logger.error(f"Holiday type '{holiday_type}' not supported.")
                    raise Exception(f"Holiday type '{holiday_type}' not supported")

            else:
                logger.error(f"Holiday type required!.")
                raise Exception(f"Holiday type required!")

        return self.created_objects


class HolidayFactoryInterface(ABC):

    @abstractmethod
    def get_holiday(self):
        raise NotImplementedError()

    @abstractmethod
    def generate_dates(self):
        raise NotImplementedError()

    @abstractmethod
    def check_holiday(self):
        raise NotImplementedError()

class PublicHoliday(HolidayFactoryInterface):
    def __init__(self, holiday_rule, start_date, end_date):
        self.holiday_rule = holiday_rule
        self.start_date = start_date
        self.end_date = end_date

    def get_holiday(self):
        return self.generate_dates(**self.holiday_rule)

    def generate_dates(self, *args, **kwargs):
        period = self.end_date.year - self.start_date.year
        try:
            is_valid = self.check_holiday(*args, **kwargs)
            if is_valid:
                month, day = kwargs.get('month'), kwargs.get('day')
                # Iterate through each year within the gap and calculate the holiday date for each year
                generated_holidays = DayUtils.generates_dates_frequency_for_certain_period(start_date=self.start_date,
                                                                                           period=period,
                                                                                           month=month,
                                                                                           day=day)
                return generated_holidays
            else:
                return []
        except Exception as e:
            return  []

    def check_holiday(self, *args, **kwargs):
        month, day = kwargs.get('month'), kwargs.get('day')

        if not month or not day:
            raise Exception("Month and day arguments are required.")

        if month < 1 or month > 12 or day < 1 or month > 31:
            raise Exception("Month and day arguments are required.")

        return True

class MoveableHoliday(HolidayFactoryInterface):
    def __init__(self, holiday_rule, start_date, end_date):
        self.holiday_rule = holiday_rule
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def move_date(date):
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

    def generate_dates(self, *args, **kwargs):
        period = self.end_date.year - self.start_date.year
        try:
            is_valid = self.check_holiday(*args, **kwargs)
            if is_valid:
                month, day = kwargs.get('month'), kwargs.get('day')
                generated_holidays = DayUtils.generates_dates_frequency_for_certain_period(start_date=self.start_date,
                                                                                        period=period,
                                                                                        month=month,
                                                                                        day=day)
                moved_dates = [self.move_date(moveable_holiday) for moveable_holiday in generated_holidays]
                return moved_dates
            else:
                return []
        except Exception as e:
            return []

    def get_holiday(self):
        return self.generate_dates(**self.holiday_rule)


    def check_holiday(self, *args, **kwargs):
        month, day = kwargs.get('month'), kwargs.get('day')

        if not month or not day:
            raise Exception("Month and day arguments are required.")

        if month<1 or month>12 or day<1 or month>31:
            raise Exception("Month and day arguments are required.")

        return True

class CertainOccurrenceHoliday(HolidayFactoryInterface):
    def __init__(self, holiday_rule, start_date, end_date):
        self.holiday_rule = holiday_rule
        self.start_date = start_date
        self.end_date = end_date

    def get_holiday(self):
        """
        Logic for certain occurrence holidays (e.g., second Monday in October).
        You need to implement the logic for calculating these holidays.
        :return: Date object or None.
        """
        # Example: Getting the second Monday in October
        return self.generate_dates(**self.holiday_rule)

    def generate_dates(self, *args, **kwargs):
        period = self.end_date.year - self.start_date.year
        try:
            is_valid = self.check_holiday(*args, **kwargs)
            if is_valid:
                month, weekday, occurrence = kwargs.get('month'), kwargs.get('day'), kwargs.get('occurrence')
                generated_holidays = DayUtils.generates_occurrence_dates_frequency_for_certain_period(start_date=self.start_date,
                                                                                                      period=period,
                                                                                                      month=month,
                                                                                                      day=weekday,
                                                                                                      occurrence=occurrence)
                return generated_holidays
            else:
                return []
        except Exception as e:
            return []

    def check_holiday(self, *args, **kwargs):
        month, day, occurrence = kwargs.get('month'), kwargs.get('day'), kwargs.get('occurrence')

        if not month and not day and occurrence:
            raise Exception("Month, Weekday and Occurrence required")

        if month < 1 or month > 12 or day < 1 or month > 31:
            raise Exception("Month and day arguments are required.")

        return True
