from python_solution.src.date_utils import DayUtils
from python_solution.src.factory import HolidayFactory
import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',  # Append to the file
)

class BusinessDayCounter:
    def __init__(self):
        super().__init__()


    # def business_days_between_two_dates(self, start_date, end_date, holiday_rules):
    #     total_days = self.days_count_between_dates(start_date=start_date, end_date=end_date)
    #     total_weekend_days = self.total_weekend_days_count(start_date=start_date,
    #                                                             total_days=total_days)
    #     holiday_factory = HolidayFactory(start_date=start_date, end_date=end_date, holiday_rules=holiday_rules)
    #     public_holiday_list = holiday_factory.generate_holiday()
    #     public_holidays = PublicHolidayCounter(start_date=start_date, end_date=end_date, public_holiday_list=public_holiday_list).get_holiday_date()
    #     total_business_days = total_days - total_weekend_days - public_holidays
    #     logging.info(f"Total days: {total_days}, Weekend days: {total_weekend_days}, Business: {total_business_days}")
    #     return total_business_days

    def business_days_between_two_dates(self, start_date, end_date, holiday_rules):
        """
        Calculate the number of business days between two dates, excluding weekends and public holidays.

        :param start_date: The start date of the range.
        :param end_date: The end date of the range.
        :param holiday_rules: Rules defining the holidays.
        :return: Total number of business days.
        """
        logging.info(f"Calculating business days between {start_date} and {end_date}.")

        date_utils = DayUtils()

        total_days = date_utils.days_count_between_dates(start_date=start_date, end_date=end_date)
        total_weekend_days = date_utils.total_weekend_days_count(start_date=start_date, total_days=total_days)

        holiday_objects = HolidayFactory(start_date=start_date, end_date=end_date, holiday_rules=holiday_rules).get_objects()
        public_holiday_list = [item for sublist in holiday_objects for item in sublist.get_holiday()]

        public_holidays = date_utils.calculate_public_holidays(start_date=start_date, end_date=end_date,
                                                                    public_holiday_list=public_holiday_list)

        total_business_days = total_days - total_weekend_days - public_holidays

        logging.info(
            f"Calculation summary:\n"
            f"  - Total days: {total_days}\n"
            f"  - Weekend days: {total_weekend_days}\n"
            f"  - Public holidays: {public_holidays}\n"
            f"  - Business days: {total_business_days}"
        )
        return total_business_days

if __name__ == '__main__':
    # # 25th of december 2013
    # first_public_holiday = datetime.date(12, 25)
    #
    # # 26th of december 2013
    # second_public_holiday = datetime.date(2013, 12, 26)
    #
    # # 1st of january 2014
    # third_public_holiday = datetime.date(2014, 1, 1)
    #
    # public_holidays = [first_public_holiday, second_public_holiday, third_public_holiday]

    holiday_rules = [
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

    # 7th of October - 9th of October -1
    # start_date = datetime.date(2013, 10, 7)
    # end_date = datetime.date(2013, 10, 9)

    # 24th of December - 27th of December 0
    start_date = datetime.date(2023, 6, 5)
    end_date = datetime.date(2023, 6, 13)


    # 7th of October - 1st of October, 2024 4
    # start_date = datetime.date(2023, 6, 9)
    # end_date = datetime.date(2023, 6, 14)
    # holiday_factory = HolidayFactory(start_date=start_date, end_date=end_date, holiday_rules=holiday_rules)
    # public_holidays_object_lists = holiday_factory.generate_holiday()

    try:
        business_day_counter = BusinessDayCounter()
        total_work_days = business_day_counter.business_days_between_two_dates(start_date, end_date, holiday_rules)
        print(total_work_days)
    except ValueError:
        print("Error raised, invalid type of dates")

