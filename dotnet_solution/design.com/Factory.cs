using System;
using System.Collections.Generic;
using System.Linq;

namespace design.com
{

    /// <summary>
    /// The HolidayFactory class is responsible for creating different types of holiday objects
    /// based on the provided holiday rules. It handles the instantiation of moveable holidays,
    /// public holidays, and certain occurrence holidays within a given date range.
    /// </summary>
    public class HolidayFactory
    {
        private List<Dictionary<string, object>> _holidayRules;
        private DateTime _startDate;
        private DateTime _endDate;
        private List<IHolidayFactoryInterface> _createdObjects = [];


        /// <summary>
        /// Initializes a new instance of the HolidayFactory class with the specified holiday rules,
        /// start date, and end date.
        /// </summary>
        /// <param name="holidayRules">A list of holiday rules, each represented by a dictionary containing the necessary details.</param>
        /// <param name="startDate">The start date of the period to consider for holiday generation.</param>
        /// <param name="endDate">The end date of the period to consider for holiday generation.</param>
        public HolidayFactory(List<Dictionary<string, object>> holidayRules, DateTime startDate, DateTime endDate)
        {
            _holidayRules = holidayRules;
            _startDate = startDate;
            _endDate = endDate;
            _createdObjects = new List<IHolidayFactoryInterface>();
        }


        /// <summary>
        /// Processes the holiday rules and creates the corresponding holiday objects based on the holiday type.
        /// </summary>
        /// <returns>A list of holiday objects, each implementing IHolidayFactoryInterface.</returns>
        /// <exception cref="Exception">Throws an exception if an unsupported holiday type is encountered or if the holiday type is missing.</exception>
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

    /// <summary>
    /// Represents a public holiday. This class validates the holiday rule and generates the dates 
    /// for a public holiday occurring every year on a fixed day and month.
    /// </summary>
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

        /// <summary>
        /// Generates the dates for the public holiday that occur every year on the specified day and month.
        /// </summary>
        /// <returns>A list of DateTime objects representing the dates of the public holiday.</returns>
        public List<DateTime> GetHoliday()
        {
            return GenerateDates(_holidayRule);
        }

        /// <summary>
        /// Generates the dates for the public holiday over a specific period.
        /// </summary>
        /// <param name="holidayRule">A dictionary containing the holiday rule details.</param>
        /// <returns>A list of DateTime objects representing the generated dates for the public holiday.</returns>
        public List<DateTime> GenerateDates(Dictionary<string, object> holidayRule)
        {
            int period = _endDate.Year - _startDate.Year;

            bool isValid = CheckHolidayRule(holidayRule: holidayRule);

            int month = (int)holidayRule["month"];
            int day = (int)holidayRule["day"];
            return DayUtils.GeneratesDatesFrequencyForCertainPeriod(_startDate, period, month, day);

        }
    }


    /// <summary>
    /// Represents a moveable holiday. This class validates the holiday rule and generates the dates 
    /// for a holiday that may change each year, depending on the day of the week.
    /// </summary>
    public class MoveableHoliday : IHolidayFactoryInterface
    {
        private Dictionary<string, object> _holidayRule;
        private DateTime _startDate;
        private DateTime _endDate;


        /// <summary>
        /// Initializes a new instance of the MoveableHoliday class with the specified holiday rule, start date, and end date.
        /// </summary>
        /// <param name="holidayRule">A dictionary containing the holiday rule details.</param>
        /// <param name="startDate">The start date of the holiday period.</param>
        /// <param name="endDate">The end date of the holiday period.</param>
        public MoveableHoliday(Dictionary<string, object> holidayRule, DateTime startDate, DateTime endDate)
        {
            _holidayRule = holidayRule;
            _startDate = startDate;
            _endDate = endDate;
        }


        /// <summary>
        /// Generates the dates for the moveable holiday, ensuring that holidays that fall on weekends are moved to the next weekday.
        /// </summary>
        /// <returns>A list of DateTime objects representing the moveable holidays.</returns>
        public List<DateTime> GetHoliday()
        {
            return GenerateDates(_holidayRule);
        }


        /// <summary>
        /// Validates the holiday rule for the moveable holiday. Ensures that both 'month' and 'day' keys are present.
        /// </summary>
        /// <param name="holidayRule">A dictionary containing the holiday rule details.</param>
        /// <returns>True if the holiday rule is valid; otherwise, throws an exception.</returns>
        /// <exception cref="Exception">Throws an exception if the month or day values are invalid.</exception>
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

        /// <summary>
        /// Generates the dates for the moveable holiday over a specific period and adjusts for weekends.
        /// </summary>
        /// <param name="holidayRule">A dictionary containing the holiday rule details.</param>
        /// <returns>A list of DateTime objects representing the moveable holidays.</returns>
        public List<DateTime> GenerateDates(Dictionary<string, object> holidayRule)
        {
            int period = _endDate.Year - _startDate.Year;
            bool isValid = CheckHolidayRule(holidayRule: holidayRule);
            int month = (int)holidayRule["month"];
            int day = (int)holidayRule["day"];
            var generatedHolidays = DayUtils.GeneratesDatesFrequencyForCertainPeriod(_startDate, period, month, day);
            return generatedHolidays.Select(moveableHoliday => MoveDate(moveableHoliday)).ToList();
        }

        /// <summary>
        /// Moves the given date to the next Monday if it falls on a weekend (Saturday or Sunday).
        /// </summary>
        /// <param name="date">The original date to be moved.</param>
        /// <returns>A new DateTime object representing the date moved to the next Monday if it was on a weekend,
        /// or the original date if it was not on a weekend.</returns>
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



    /// <summary>
    /// Represents a holiday that occurs on a specific occurrence, such as the second Monday of a month.
    /// This class generates dates for such holidays based on their occurrence in a specific month.
    /// </summary>
    public class CertainOccurrenceHoliday : IHolidayFactoryInterface
    {
        private Dictionary<string, object> _holidayRule;
        private DateTime _startDate;
        private DateTime _endDate;


        /// <summary>
        /// Initializes a new instance of the CertainOccurrenceHoliday class with the specified holiday rule, start date, and end date.
        /// </summary>
        /// <param name="holidayRule">A dictionary containing the holiday rule details.</param>
        /// <param name="startDate">The start date of the holiday period.</param>
        /// <param name="endDate">The end date of the holiday period.</param>

        public CertainOccurrenceHoliday(Dictionary<string, object> holidayRule, DateTime startDate, DateTime endDate)
        {
            _holidayRule = holidayRule;
            _startDate = startDate;
            _endDate = endDate;
        }


        /// <summary>
        /// Validates the holiday rule for the occurrence-based holiday.
        /// </summary>
        /// <param name="holidayRule">A dictionary containing the holiday rule details.</param>
        /// <returns>True if the holiday rule is valid; otherwise, throws an exception.</returns>
        public bool CheckHolidayRule(Dictionary<string, object> holidayRule)
        {
            if (!holidayRule.ContainsKey("month") || !holidayRule.ContainsKey("occurrence") || !holidayRule.ContainsKey("day"))
            {
                throw new Exception("Both 'month' and 'occurrence' and 'day' keys are required in the holidayRule dictionary.");
            }
            int month = (int)holidayRule["month"];
            int occurrence = (int)holidayRule["occurrence"];
            int day = (int)holidayRule["day"];

            if (month == 0 || occurrence == 0)
            {
                throw new Exception("Month and occurrence arguments are required. !!");
            }

            if (month < 1 || month > 12 || day > 6 || day < 0)
            {
                throw new Exception("Invalid month or day or occurrence values. !!");
            }

            return true;
        }



        /// <summary>
        /// Generates the dates for the occurrence-based holiday within the specified period.
        /// </summary>
        /// <returns>A list of DateTime objects representing the occurrence-based holidays.</returns>
        public List<DateTime> GetHoliday()
        {
            return GenerateDates(_holidayRule);
        }


        /// <summary>
        /// Generates the dates for the occurrence-based holiday over a specific period.
        /// </summary>
        /// <param name="holidayRule">A dictionary containing the holiday rule details.</param>
        /// <returns>A list of DateTime objects representing the occurrence-based holidays.</returns>
        public List<DateTime> GenerateDates(Dictionary<string, object> holidayRule)
        {

            int period = _endDate.Year - _startDate.Year;
            bool isValid = CheckHolidayRule(holidayRule: holidayRule);
            int month = (int)holidayRule["month"];
            int day = (int)holidayRule["day"];
            int occurrence = (int)holidayRule["occurrence"];
            return DayUtils.GeneratesOccurrenceDatesFrequencyForCertainPeriod(startDate: _startDate,
                                                                            period: period,
                                                                            month: month,
                                                                            day: day,
                                                                            occurrence: occurrence);

        }
    }
}
