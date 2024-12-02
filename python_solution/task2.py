
import datetime
import logging

from src.business_day_counter import BusinessDayCounter
from src.date_utils import DayUtils

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run(start_end_date_list, public_holiday_list):
    """
    This function just written that to run and see code works.

    :param start_end_date_list:
    :return:
    """
    day_utils_obj = DayUtils()

    case_number = 0

    for _date_list in start_end_date_list:
        case_number += 1
        start_date = _date_list.get('start_date')
        end_date = _date_list.get('end_date')

        logging.info("=" * 50)
        logging.info("Running Task 2: Business Days Between Two Dates")
        logging.info("=" * 50)

        if public_holiday_list is None:
            logging.info("Please enter public_holidays list")
            continue

        if start_date is None or end_date is None:
            logging.info("You should enter both start and end dates")
            continue

        logging.info(f"Start date: {start_date}, End date: {end_date}")
        business_day_counter = BusinessDayCounter(day_utils_obj=day_utils_obj)
        total_work_days = business_day_counter.business_days_between_two_dates(start_date, end_date,
                                                                               public_holiday_list=public_holiday_list)

        logging.info("=" * 50)
        logging.info(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
        logging.info(f"End Date  : {end_date.strftime('%Y-%m-%d')}")
        logging.info(f"Business Days  : {total_work_days}")
        logging.info("=" * 50)


if __name__ == '__main__':

    try:
        # 25th of december 2013
        first_public_holiday = datetime.date(2013, 12, 25)
        # 26th of december 2013
        second_public_holiday = datetime.date(2013, 12, 26)
        # 1st of january 2014
        third_public_holiday = datetime.date(2014, 1, 1)
        start_end_date_list = [
            {
                "start_date": datetime.date(2013, 10, 7),
                "end_date": datetime.date(2013, 10, 9) # Result must be 1
            },
            {
                "start_date": datetime.date(2013, 12, 24),
                "end_date": datetime.date(2013, 12, 27) # Result must be 0
            },
            {
                "start_date": datetime.date(2013, 10, 7),
                "end_date": datetime.date(2014, 1, 1)  # Result must be 59
            }
        ]


        public_holiday_list = [
            first_public_holiday,
            second_public_holiday,
            third_public_holiday
        ]

        run(start_end_date_list, public_holiday_list)

    except ValueError as e:
        logging.error("Please enter valid date {}".format(e))
