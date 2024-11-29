import datetime

holiday1 = datetime.date(2013, 12, 25)
holiday2 = datetime.date(2013, 12, 26)
holiday3 = datetime.date(2014, 1, 1)

holiday_list = [
    {
        "date": holiday1,
        "is_weekday": True if holiday1.weekday() < 5 else False,
    },
    {
        "date": holiday2,
        "is_weekday": True if holiday2.weekday() < 5 else False,
    },
    {
        "date": holiday3,
        "is_weekday": True if holiday2.weekday() < 5 else False,
    }
]
#This challenge is concerned with counting the number of days between two dates.
class BusinessDayCounter:
    def __init__(self, end_date, start_date):
        self.workdays_count = 0
        self.result = 0
        self.end_date = end_date
        self.start_date = start_date
        self.number_of_days_in_a_week = 7
        self.gap_total_days_count = (self.end_date - self.start_date).days - 1

    @property
    def check_dates_are_same(self):
        return 0 if self.start_date >= self.end_date else 1

    @property
    def remainder(self):
        """
        Finds to remainder, if the remainder not equal to zero, we should check that begin and end dates to calculate
        exact calculation
        :return:
        """
        return 0 if self.gap_total_days_count < self.number_of_days_in_a_week else self.gap_total_days_count % self.number_of_days_in_a_week

    @property
    def quotient(self):
        """
        Finds to quotient to understand how many weekends past
        :return: @type int
        """
        return self.gap_total_days_count // self.number_of_days_in_a_week

    @property
    def weekends_days(self):
        """
        It's calculate the weekends days for each weekends
        :return: @type int
        """
        weekends_days = 0
        if self.remainder != 0:
            if self.start_date.weekday() == 5:
                weekends_days += 1
            if  self.end_date.weekday() == 6:
                weekends_days += 1
        weekends_days = self.quotient * 2 + weekends_days
        return weekends_days

    def weekdays_between_two_dates(self):
        self.workdays_count = self.gap_total_days_count - self.weekends_days
        return self.workdays_count

    def run(self):
        dates_same_or_invalid = self.check_dates_are_same
        if not dates_same_or_invalid:
            return dates_same_or_invalid
        else:
            return self.weekdays_between_two_dates()

    def business_days_between_two_days(self):
        self.weekdays_between_two_dates()
        for holiday in holiday_list:
            if not (holiday["date"] == self.start_date or holiday["date"] == self.end_date) and holiday["is_weekday"] and (self.start_date< holiday['date'] < self.end_date) :
                self.workdays_count += -1
            else:
                pass
        return self.workdays_count

if __name__ == "__main__":

    start_date = datetime.date(2013, 10, 7)
    end_date = datetime.date(2014, 1, 1)
    business_day_counter = BusinessDayCounter(start_date=start_date, end_date=end_date)
    value = business_day_counter.business_days_between_two_days()
    print(value)