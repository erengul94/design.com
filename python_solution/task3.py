
import datetime
import logging

from src.business_day_counter import BusinessDayCounter
from src.date_utils import DayUtils

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run(start_end_date_list, holiday_rules):
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

        if holiday_rules is None:
            logging.info("Please enter holiday_rules list")
            continue

        if start_date is None or end_date is None:
            logging.info("You should enter both start and end dates")
            continue

        logging.info(f"Start date: {start_date}, End date: {end_date}")
        business_day_counter = BusinessDayCounter(day_utils_obj=day_utils_obj)
        total_work_days = business_day_counter.business_days_between_two_dates(start_date, end_date,
                                                                               holiday_rules=holiday_rules)

        logging.info("=" * 50)
        logging.info(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
        logging.info(f"End Date  : {end_date.strftime('%Y-%m-%d')}")
        logging.info(f"Business Days  : {total_work_days}")
        logging.info("=" * 50)


if __name__ == '__main__':

    holiday_rules = [
        {
            "holiday_type": "public_holiday",
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

    try:
        start_end_date_list =[
            {
                "start_date": datetime.date(2022, 12, 26),
                "end_date": datetime.date(2023, 1, 3) # Result must be 4 # for new years case
            },
            {
                "start_date": datetime.date(2023, 4, 20),
                "end_date": datetime.date(2023, 4, 27) # Result must be 3 # for Anzac Day case
            },
            {
                "start_date": datetime.date(2023, 6, 9),
                "end_date": datetime.date(2023, 6, 15)  # Result must be 2 # for Queens Day case
            }
        ]
        run(start_end_date_list, holiday_rules)

    except ValueError as e:
        logging.error("Please enter valid date {}".format(e))
