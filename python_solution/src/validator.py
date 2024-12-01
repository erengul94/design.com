import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def validate_dates(func):
    """
    Annotation to validate the start_date and end_date parameters for a function.
    Ensures the following:
    - Both dates are of type datetime.date.
    - Both dates are valid calendar dates.
    - The start_date is earlier than the end_date.
    If validation fails, a ValueError is raised or a default result of 0 is returned.

    Logs validation results and errors for better debugging.

    :param func: Function to wrap
    :return: Result of the decorated function or 0 if dates are invalid
    """
    def wrapper(start_date, end_date):
        logger.info("Validating dates: start_date=%s, end_date=%s", start_date, end_date)

        if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
            logger.error("Invalid date types. Both start_date and end_date must be datetime.date objects.")
            raise ValueError("Both start_date and end_date must be of type datetime.date")

        try:
            datetime.date(start_date.year, start_date.month, start_date.day)
            datetime.date(end_date.year, end_date.month, end_date.day)
        except ValueError as e:
            logger.error("Invalid calendar date: %s", e)
            raise ValueError("Invalid calendar date")

        if start_date >= end_date:
            logger.warning("Invalid date range: start_date >= end_date. Returning 0.")
            return 0

        result = func(start_date, end_date)
        logger.info("Result after validation: %s", result)
        return result

    return wrapper
