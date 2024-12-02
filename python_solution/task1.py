
import datetime
import logging

from src.business_day_counter import BusinessDayCounter
from src.date_utils import DayUtils

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run(start_end_date_list):
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
        logging.info("Running Task 1: Weekdays Between Two Dates")
        logging.info("=" * 50)

        if start_date is None or end_date is None:
            logging.info("You should enter both start and end dates")
            continue

        logging.info(f"Start date: {start_date}, End date: {end_date}")

        business_day_counter = BusinessDayCounter(day_utils_obj=day_utils_obj)
        total_week_days = business_day_counter.weekdays_between_two_dates(start_date, end_date)

        logging.info("=" * 50)
        logging.info(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
        logging.info(f"End Date  : {end_date.strftime('%Y-%m-%d')}")
        logging.info(f"Weekdays  : {total_week_days}")
        logging.info("=" * 50)




if __name__ == '__main__':
    try:
        start_end_date_list = [
        {
            "start_date": datetime.date(2013, 10, 7),
            "end_date": datetime.date(2013, 10, 9) # Result must be 1
        },
        {
            "start_date": datetime.date(2013, 10, 5),
            "end_date": datetime.date(2013, 10, 14) # Result must be 5
        },
        {
            "start_date": datetime.date(2013, 10, 7),
            "end_date": datetime.date(2014, 1, 1)  # Result must be 61
        },
        {
            "start_date": datetime.date(2013, 10, 7),
            "end_date": datetime.date(2013, 10, 5)  # Result must be 0
        }
    ]
        run(start_end_date_list)
    except ValueError as e:
        logging.error("Please enter valid date {}".format(e))
