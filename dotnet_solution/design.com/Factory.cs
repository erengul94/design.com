using System;
using System.Collections.Generic;
using System.Linq;

namespace design.com
{
    public class HolidayFactory
    {
        private List<Dictionary<string, object>> _holidayRules;
        private DateTime _startDate;
        private DateTime _endDate;
        private List<IHolidayFactoryInterface> _createdObjects = [];

        public HolidayFactory(List<Dictionary<string, object>> holidayRules, DateTime startDate, DateTime endDate)
        {
            _holidayRules = holidayRules;
            _startDate = startDate;
            _endDate = endDate;
            _createdObjects = new List<IHolidayFactoryInterface>();
        }

        public List<IHolidayFactoryInterface> GetObjects()
        {
            foreach (var holidayRule in _holidayRules)
            {
                string holidayType = holidayRule.ContainsKey("holiday_type") ? holidayRule["holiday_type"].ToString() : null;

                if (!string.IsNullOrEmpty(holidayType))
                {
                    if (holidayType == "moveable_holiday")
                    {
                        _createdObjects.Add(new MoveableHoliday(holidayRule, _startDate, _endDate));
                    }
                    else if (holidayType == "public_holiday")
                    {
                        _createdObjects.Add(new PublicHoliday(holidayRule, _startDate, _endDate));
                    }
                    else if (holidayType == "certain_occurrence_holiday")
                    {
                        _createdObjects.Add(new CertainOccurrenceHoliday(holidayRule, _startDate, _endDate));
                    }
                    else
                    {
                        throw new Exception($"Holiday type '{holidayType}' not supported.");
                    }
                }
                else
                {
                    throw new Exception("Holiday type required!");
                }
            }

            return _createdObjects;
        }
    }

    public class PublicHoliday : IHolidayFactoryInterface
    {
        private Dictionary<string, object> _holidayRule;
        private DateTime _startDate;
        private DateTime _endDate;

        public PublicHoliday(Dictionary<string, object> holidayRule, DateTime startDate, DateTime endDate)
        {
            _holidayRule = holidayRule;
            _startDate = startDate;
            _endDate = endDate;
        }
        public bool CheckHolidayRule(Dictionary<string, object> holidayRule)
        {
            if (!holidayRule.ContainsKey("month") || !holidayRule.ContainsKey("day"))
            {
                throw new Exception("Both 'month' and 'day' keys are required in the holidayRule dictionary.");
            }
            int month = (int)holidayRule["month"];
            int day = (int)holidayRule["day"];

            if (month == 0 || day == 0)
            {
                throw new Exception("Month and day arguments are required.");
            }

            if (month < 1 || month > 12 || day < 1 || day > 31)
            {
                throw new Exception("Invalid month or day values.");
            }

            return true;
        }

        public List<DateTime> GetHoliday()
        {
            return GenerateDates(_holidayRule);
        }

        public List<DateTime> GenerateDates(Dictionary<string, object> holidayRule)
        {
            int period = _endDate.Year - _startDate.Year;
            try
            {
                bool isValid = CheckHolidayRule(holidayRule: holidayRule);
                if (isValid)
                {
                    int month = (int)holidayRule["month"];
                    int day = (int)holidayRule["day"];
                    return DayUtils.GeneratesDatesFrequencyForCertainPeriod(_startDate, period, month, day);
                }
                else
                {
                    return new List<DateTime>(); // Return an empty list if validation fails
                }
            }

            catch (Exception ex)
            {
                Console.WriteLine($"Error validating holiday rule: {ex.Message}");
                return new List<DateTime>();
            }

        }
    }

    public class MoveableHoliday : IHolidayFactoryInterface
    {
        private Dictionary<string, object> _holidayRule;
        private DateTime _startDate;
        private DateTime _endDate;

        public MoveableHoliday(Dictionary<string, object> holidayRule, DateTime startDate, DateTime endDate)
        {
            _holidayRule = holidayRule;
            _startDate = startDate;
            _endDate = endDate;
        }

        public List<DateTime> GetHoliday()
        {
            return GenerateDates(_holidayRule);
        }

        public bool CheckHolidayRule(Dictionary<string, object> holidayRule)
        {
            if (!holidayRule.ContainsKey("month") || !holidayRule.ContainsKey("day"))
            {
                throw new Exception("Both 'month' and 'day' keys are required in the holidayRule dictionary.");
            }
            int month = (int)holidayRule["month"];
            int day = (int)holidayRule["day"];

            if (month == 0 || day == 0)
            {
                throw new Exception("Month and day arguments are required.");
            }

            if (month < 1 || month > 12 || day < 1 || day > 31)
            {
                throw new Exception("Invalid month or day values.");
            }

            return true;
        }
        public List<DateTime> GenerateDates(Dictionary<string, object> holidayRule)
        {
            int period = _endDate.Year - _startDate.Year;
            try
            {
                bool isValid = CheckHolidayRule(holidayRule: holidayRule);
                if (isValid)
                {
                    int month = (int)holidayRule["month"];
                    int day = (int)holidayRule["day"];
                    var generatedHolidays = DayUtils.GeneratesDatesFrequencyForCertainPeriod(_startDate, period, month, day);
                    return generatedHolidays.Select(moveableHoliday => MoveDate(moveableHoliday)).ToList();
                }
                else
                {
                    return new List<DateTime>();
                };

            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error validating holiday rule: {ex.Message}");
                return new List<DateTime>();
            }

        }

        private static DateTime MoveDate(DateTime date)
        {
            if (date.DayOfWeek == DayOfWeek.Saturday)
            {
                date = date.AddDays(2); // Move to Monday
            }
            else if (date.DayOfWeek == DayOfWeek.Sunday)
            {
                date = date.AddDays(1); // Move to Monday
            }
            return date;
        }
    }

    public class CertainOccurrenceHoliday : IHolidayFactoryInterface
    {
        private Dictionary<string, object> _holidayRule;
        private DateTime _startDate;
        private DateTime _endDate;

        public CertainOccurrenceHoliday(Dictionary<string, object> holidayRule, DateTime startDate, DateTime endDate)
        {
            _holidayRule = holidayRule;
            _startDate = startDate;
            _endDate = endDate;
        }

        public bool CheckHolidayRule(Dictionary<string, object> holidayRule)
        {
            if (!holidayRule.ContainsKey("month") || !holidayRule.ContainsKey("day") || !holidayRule.ContainsKey("occurrence"))
            {
                throw new Exception("Both 'month' and 'day' keys are required in the holidayRule dictionary.");
            }
            int month = (int)holidayRule["month"];
            int day = (int)holidayRule["day"];
            int occurrence = (int)holidayRule["occurrence"];


            if (month == 0 || day == 0 || occurrence == 0)
            {
                throw new Exception("Month and day arguments are required.");
            }

            if (month < 1 || month > 12 || day < 1 || day > 31 || occurrence > 4) // max 4 weeks in a month
            {
                throw new Exception("Invalid month or day or occurrence values.");
            }

            return true;
        }


        public List<DateTime> GetHoliday()
        {
            return GenerateDates(_holidayRule);
        }

        public List<DateTime> GenerateDates(Dictionary<string, object> holidayRule)
        {

            int period = _endDate.Year - _startDate.Year;
            try
            {

                bool isValid = CheckHolidayRule(holidayRule: holidayRule);
                if (isValid)
                {
                    int month = (int)holidayRule["month"];
                    int day = (int)holidayRule["day"];
                    int occurrence = (int)holidayRule["occurrence"];
                    return DayUtils.GeneratesOccurrenceDatesFrequencyForCertainPeriod(startDate: _startDate,
                    period: period, month: month, day: day, occurrence: occurrence);
                }
                else { return new List<DateTime>(); }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error validating holiday rule: {ex.Message}");
                return new List<DateTime>();
            }
        }
    }
}
