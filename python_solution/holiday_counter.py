
from abc import ABC, abstractmethod


class HolidayCounter(ABC):
    def __init__(self):
        self.week_days_range = {0, 1, 2, 3, 4} # Monday, Tuesday... Friday
        self.weekend_days_range = {5, 6}

    @abstractmethod
    def get_holiday_date(self):
        raise NotImplementedError("You must implement this method")

class PublicHolidayCounter(HolidayCounter):
    def __init__(self, start_date, end_date, public_holiday_list):
        super().__init__()
        self.start_date = start_date
        self.end_date = end_date
        self.public_holiday_list = public_holiday_list
        self.public_holiday_days_total_count = 0

    def get_holiday_date(self):
        for holiday in self.public_holiday_list:
            if (holiday.weekday() in self.week_days_range) and (self.start_date < holiday < self.end_date):
                self.public_holiday_days_total_count += 1
        return self.public_holiday_days_total_count



