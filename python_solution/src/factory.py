from abc import abstractmethod, ABC
from datetime import timedelta
from src.date_utils import DayUtils
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HolidayFactory(object):
    """
    A factory class responsible for creating holiday objects based on different holiday rules and a given date range.

    Attributes:
        holiday_rules (list): A list of holiday rule dictionaries.
        created_objects (list): A list of created holiday objects.
        start_date (datetime): The start date for the holiday generation.
        end_date (datetime): The end date for the holiday generation.

    Methods:
        get_objects(): Creates and returns a list of holiday objects based on the provided rules.
    """

    def __init__(self, holiday_rules, start_date, end_date):
        self.holiday_rules = holiday_rules
        self.created_objects = []
        self.start_date = start_date
        self.end_date = end_date

    def get_objects(self):
        """
        Creates holiday objects based on the provided holiday rules and returns them.

        Returns:
            list: A list of created holiday objects based on the rules (e.g., MoveableHoliday, PublicHoliday, CertainOccurrenceHoliday).

        Raises:
            Exception: If the holiday type in the rule is unsupported or missing.
        """
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
    """
    An abstract base class defining the interface for holiday objects.
    Derived classes must implement the following methods:
        - get_holiday(): Retrieves the holiday dates.
        - generate_dates(): Generates holiday dates based on specific rules.
        - check_holiday(): Validates the holiday rule parameters.
    """
    @abstractmethod
    def get_holiday(self):
        """
            Retrieves the holiday dates based on the implemented logic.
        """
        raise NotImplementedError()

    @abstractmethod
    def generate_dates(self):
        """
            Generates holiday dates based on specific holiday rules.
        """
        raise NotImplementedError()

    @abstractmethod
    def check_holiday(self):
        """
          Validates the holiday rule parameters.
        """
        raise NotImplementedError()

class PublicHoliday(HolidayFactoryInterface):
    """
     A class representing a public holiday, implementing the HolidayFactoryInterface.
     Generates dates for a specific public holiday based on the provided month and day.

     Methods:
         get_holiday(): Returns a list of public holiday dates for each year in the specified period.
         generate_dates(): Generates a list of holiday dates based on the month and day.
         check_holiday(): Validates the month and day values for correctness.
     """
    def __init__(self, holiday_rule, start_date, end_date):
        """
          Initializes the PublicHoliday object with a holiday rule, start date, and end date.

          Args:
              holiday_rule (dict): A dictionary containing holiday rule details.
              start_date (datetime): The start date for generating holidays.
              end_date (datetime): The end date for generating holidays.
          """
        self.holiday_rule = holiday_rule
        self.start_date = start_date
        self.end_date = end_date

    def get_holiday(self):
        """
           Generates and returns public holiday dates.

           Returns:
               list: A list of generated public holiday dates.
           """
        return self.generate_dates(**self.holiday_rule)

    def generate_dates(self, *args, **kwargs):
        """
               Generates public holiday dates within the specified date range, adjusted for the period.

               Args:
                   *args: Additional arguments.
                   **kwargs: Keyword arguments containing month and day values.

               Returns:
                   list: A list of generated holiday dates, or an empty list if the parameters are invalid.
               """
        period = self.end_date.year - self.start_date.year
        is_valid = self.check_holiday(*args, **kwargs)
        if is_valid:
            month, day = kwargs.get('month'), kwargs.get('day')
            generated_holidays = DayUtils.generates_dates_frequency_for_certain_period(start_date=self.start_date,
                                                                                       period=period,
                                                                                       month=month,
                                                                                       day=day)
            return generated_holidays


    def check_holiday(self, *args, **kwargs):
        """
        Validates the month and day values for correctness.

        Args:
            *args: Additional arguments.
            **kwargs: Keyword arguments containing month and day values.

        Returns:
            bool: True if the parameters are valid, otherwise raises an exception.

        Raises:
            Exception: If the month or day values are invalid.
        """
        month, day = kwargs.get('month'), kwargs.get('day')

        if not month or not day:
            raise Exception("Month and day arguments are required. !!")

        if month < 1 or month > 12 or day < 1 or month > 31:
            raise Exception("Month and day must be in valid range !!.")

        return True

class MoveableHoliday(HolidayFactoryInterface):
    """
    A class representing a moveable holiday, implementing the HolidayFactoryInterface.
    Generates dates for a specific moveable holiday and adjusts them if they fall on a weekend.

    Methods:
        move_date(): Adjusts a holiday date if it falls on a weekend (Saturday or Sunday).
        generate_dates(): Generates a list of moveable holiday dates.
        get_holiday(): Returns the adjusted holiday dates.
        check_holiday(): Validates the month and day values for correctness.
    """
    def __init__(self, holiday_rule, start_date, end_date):
        """
           Initializes the MoveableHoliday object with a holiday rule, start date, and end date.

           Args:
               holiday_rule (dict): A dictionary containing holiday rule details.
               start_date (datetime): The start date for generating holidays.
               end_date (datetime): The end date for generating holidays.
           """
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
        """
         Generates moveable holiday dates within the specified date range and adjusts for weekends.

         Args:
             *args: Additional arguments.
             **kwargs: Keyword arguments containing month and day values.

         Returns:
             list: A list of adjusted moveable holiday dates.
         """
        period = self.end_date.year - self.start_date.year
        is_valid = self.check_holiday(*args, **kwargs)
        if is_valid:
            month, day = kwargs.get('month'), kwargs.get('day')
            generated_holidays = DayUtils.generates_dates_frequency_for_certain_period(start_date=self.start_date,
                                                                                       period=period,
                                                                                       month=month,
                                                                                       day=day)
            moved_dates = [self.move_date(moveable_holiday) for moveable_holiday in generated_holidays]
            return moved_dates

    def get_holiday(self):
        """
           Returns the moveable holiday dates, adjusted for weekends.

           Returns:
               list: A list of adjusted moveable holiday dates.
           """
        return self.generate_dates(**self.holiday_rule)


    def check_holiday(self, *args, **kwargs):
        """
           Validates the month and day values for correctness.

           Args:
               *args: Additional arguments.
               **kwargs: Keyword arguments containing month and day values.

           Returns:
               bool: True if the parameters are valid, otherwise raises an exception.

           Raises:
               Exception: If the month or day values are invalid.
           """
        month, day = kwargs.get('month'), kwargs.get('day')

        if not month or not day:
            raise Exception("Month and day arguments are required. !!")

        if month<1 or month>12 or day<1 or month>31:
            raise Exception("Month and day must be valid range !!.")

        return True

class CertainOccurrenceHoliday(HolidayFactoryInterface):
    """
      A class representing a holiday that occurs on a certain weekday of a specific month, implementing the HolidayFactoryInterface.
      Generates dates for this specific occurrence holiday within the given date range.

      Methods:
          get_holiday(): Returns a list of dates for the specific occurrence of the holiday.
          generate_dates(): Generates a list of dates for the specific occurrence of the holiday.
          check_holiday(): Validates the weekday and month values for correctness.
      """
    def __init__(self, holiday_rule, start_date, end_date):
        """
            Initializes the CertainOccurrenceHoliday object with a holiday rule, start date, and end date.

            Args:
                holiday_rule (dict): A dictionary containing holiday rule details.
                start_date (datetime): The start date for generating holidays.
                end_date (datetime): The end date for generating holidays.
            """
        self.holiday_rule = holiday_rule
        self.start_date = start_date
        self.end_date = end_date

    def get_holiday(self):
        """
            Generates and returns dates for the specific occurrence holiday.

            Returns:
                list: A list of dates for the specific occurrence of the holiday.
            """
        # Example: Getting the second Monday in October
        return self.generate_dates(**self.holiday_rule)

    def generate_dates(self, *args, **kwargs):
        """
           Generates dates for a certain occurrence of a holiday based on weekday and month.

           Args:
               *args: Additional arguments.
               **kwargs: Keyword arguments containing weekday and month details.

           Returns:
               list: A list of dates for the specific occurrence of the holiday.
           """
        period = self.end_date.year - self.start_date.year
        is_valid = self.check_holiday(*args, **kwargs)
        if is_valid:
            month, weekday, occurrence = kwargs.get('month'), kwargs.get('day'), kwargs.get('occurrence')
            generated_holidays = DayUtils.generates_occurrence_dates_frequency_for_certain_period(
                start_date=self.start_date,
                period=period,
                month=month,
                day=weekday,
                occurrence=occurrence)
            return generated_holidays

    def check_holiday(self, *args, **kwargs):
        """
           Validates the weekday and month values for correctness.

           Args:
               *args: Additional arguments.
               **kwargs: Keyword arguments containing weekday and month values.

           Returns:
               bool: True if the parameters are valid, otherwise raises an exception.

           Raises:
               Exception: If the weekday or month values are invalid.
           """
        month, day, occurrence = kwargs.get('month'), kwargs.get('day'), kwargs.get('occurrence')

        if not month and occurrence and day:
            raise Exception("Month and Occurrence and day required !!")

        if not 0 < month < 12 and not 0 <= day < 7 :
            raise Exception("Month and day must be valid range !!.")

        return True
