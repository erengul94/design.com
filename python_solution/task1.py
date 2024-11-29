import datetime
import logging

from day_calculator import DayCalculator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

class BusinessDayCounter(DayCalculator):
    def __init__(self):
        super().__init__()

    def weekdays_between_two_dates(self, start_date, end_date):
        """
        This methods calculates the number of weekdays between two dates.
        :param start_date: @type object -> datetime, which indicates start date of between two dates.
        :param end_date: @type object -> datetime, which indicates start date of between two dates.
        :return: @types int
        """
        logging.info(f"Calculating weekdays between {start_date} and {end_date}.")
        total_days = self.days_count_between_dates(start_date=start_date, end_date=end_date)
        total_weekend_days = self.total_weekend_days_count(start_date=start_date, total_days=total_days)
        total_week_days = total_days - total_weekend_days
        logging.info(f"Total days: {total_days}, Weekend days: {total_weekend_days}, Weekdays: {total_week_days}")
        return total_week_days


if __name__ == '__main__':

    # 7th of October - 9th of October - 1
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 1, 10)

    # 5th of October - 14th of October -5
    # start_date = datetime.date(2013, 10, 5)
    # end_date = datetime.date(2013, 10, 14)


    # 7th of October - 1st of October, 2024 -61
    # start_date = datetime.date(2013, 10, 7)
    # end_date = datetime.date(2014, 1, 1)

    # 7th of October - 5st of October - 0
    # start_date = datetime.date(2013, 10, 7)
    # end_date = datetime.date(2013, 10, 7)
    #
    # start_date = "1,3,4"
    # end_date = "1,3,4"

    try:
        if start_date and end_date:
            logging.info(f"Start date: {start_date}, End date: {end_date}")
            business_day_counter = BusinessDayCounter()
            total_work_days = business_day_counter.weekdays_between_two_dates(start_date, end_date)
            logging.info(total_work_days)
            logging.info(f"Total weekdays between {start_date} and {end_date}: {total_work_days}")
        else:
            logging.warning("Start date or end date is missing.")
            logging.info('Please enter start date and end date')
    except ValueError as e:
        logging.error(f"ValueError encountered: {e}")
        logging.error("Error raised, invalid type of dates")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        logging.error("An unexpected error occurred. Please check the logs.")

