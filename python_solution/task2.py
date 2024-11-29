
from day_calculator import DayCalculator
from holiday_counter import PublicHolidayCounter

import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',  # Append to the file
)

class BusinessDayCounter(DayCalculator):
    def __init__(self):
        super().__init__()


    def business_days_between_two_dates(self, start_date, end_date, public_holiday_list):
        logging.info(f"Business days between {start_date} and {end_date}.")
        total_days = self.days_count_between_dates(start_date=start_date, end_date=end_date)
        total_weekend_days = self.total_weekend_days_count(start_date=start_date,
                                                           total_days=total_days)
        public_holidays = self.calculate_public_holidays(start_date=start_date, end_date=end_date,
                                                         public_holiday_list=public_holiday_list)
        total_business_days = total_days - total_weekend_days - public_holidays
        logging.info(f"Total days: {total_days}, Weekend days: {total_weekend_days}, Business: {total_business_days}")
        return total_business_days


if __name__ == '__main__':
    # 25th of december 2013
    first_public_holiday = datetime.date(2013, 12, 25)

    # 26th of december 2013
    second_public_holiday = datetime.date(2013, 12, 26)

    # 1st of january 2014
    third_public_holiday = datetime.date(2014, 1, 1)

    public_holidays = [first_public_holiday, second_public_holiday, third_public_holiday]

    # 7th of October - 9th of October -1
    start_date = datetime.date(2013, 10, 7)
    end_date = datetime.date(2013, 10, 9)

    # 24th of December - 27th of December 0
    # start_date = datetime.date(2013, 12, 24)
    # end_date = datetime.date(2013, 12, 27)


    # 7th of October - 1st of October, 2024 -59
    # start_date = datetime.date(2013, 10, 7)
    # end_date = datetime.date(2014, 1, 1)

    business_day_counter = BusinessDayCounter()
    try:
        if first_public_holiday and second_public_holiday and third_public_holiday:
            total_work_days = business_day_counter.business_days_between_two_dates(start_date, end_date, public_holidays)
            print(total_work_days)
        else:
            print('Please enter start date and end date')
    except ValueError:
        print("Error raised, invalid type of dates")

