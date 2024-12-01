
using Microsoft.Extensions.Logging;

namespace design.com
{
    public class BusinessDayCounter
    {

        private readonly DayUtils _dayUtils;
        public BusinessDayCounter(DayUtils dayUtils)
        {
            _dayUtils = dayUtils;
        }



        /// It uses a utility method to count the days, handling any invalid date ranges or exceptions that may arise.
        ///
        /// </summary>
        /// <param name="startDate">The start date of the range.</param>
        /// <param name="endDate">The end date of the range.</param>
        /// <param name="totalDays">The current total days, to which the days between the start and end date will be added.</param>
        /// <returns>The updated total days after adding the calculated number of days between the two dates. Returns 0 if an exception occurs.</returns>
        public int GetTotalDays(DateTime startDate, DateTime endDate, int totalDays){
            try
            {

                totalDays += (int)DateValidator.ValideteDates(
                _dayUtils,
                nameof(DayUtils.DaysCountBetweenDates),
                startDate,
                endDate);

            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"Exception occured while counting between days, invalid date range or invalid date entered {ex.Message}");
                return 0;
            }

            return totalDays;

        }



        /// </summary>
        /// <param name="startDate">The start date of the range.</param>
        /// <param name="endDate">The end date of the range.</param>
        /// <param name="publicHolidays">An integer representing the initial count of public holidays.</param>
        /// <param name="publicHolidaysList">A list of static public holidays (optional).</param>
        /// <param name="holidayRules">A list of dictionaries containing holiday rules (optional).</param>
        /// <returns>The updated count of public holidays between the two dates.</returns>
        public int GetHolidays(DateTime startDate, DateTime endDate, int publicHolidays,
        List<DateTime> publicHolidaysList = null, List<Dictionary<string, object>> holidayRules = null)
        {
            if (publicHolidaysList != null) 
              { 
                publicHolidays += _dayUtils.CalculatePublicHolidays(startDate, endDate, publicHolidaysList); 
                }
            if (holidayRules != null)
            {   
                List<IHolidayFactoryInterface> holidayObjects = new HolidayFactory(startDate: startDate, endDate: endDate, holidayRules: holidayRules).GetObjects();                
                List<DateTime> publicHolidayListGeneratedByRules = holidayObjects
                    .SelectMany(sublist => sublist.GetHoliday())
                    .ToList();

                publicHolidays += _dayUtils.CalculatePublicHolidays(startDate: startDate, endDate: endDate, publicHolidayList: publicHolidayListGeneratedByRules);
            }

            return publicHolidays;
        }




        /// <summary>
        /// This method calculates the number of weekdays between two dates.
        /// It considers weekends as non-working days and excludes them from the count.
        /// </summary>
        /// <param name="startDate">The start date of the range.</param>
        /// <param name="endDate">The end date of the range.</param>
        /// <returns>The number of weekdays between the two dates.</returns>

        public int WeekdaysBetweenTwoDates(DateTime startDate, DateTime endDate)
        {
            Console.WriteLine($"Calculating weekdays between {startDate} and {endDate}.");

            int totalDays = 0;
            
            totalDays += GetTotalDays(startDate:startDate, endDate:endDate, totalDays:totalDays);
            if (totalDays == 0){return 0;}

            int totalWeekendDays = _dayUtils.TotalWeekendDaysCount(startDate, totalDays);
            int totalWeekdays = totalDays - totalWeekendDays;

            Console.WriteLine($"Total days: {totalDays}, Weekend days: {totalWeekendDays}, Weekdays: {totalWeekdays}");

            return totalWeekdays;
        }



        /// <summary>
        /// This method calculates the number of business days between two dates, considering weekends and public holidays.
        /// It takes into account static public holidays and holidays based on certain rules, if provided.
        /// </summary>
        /// <param name="startDate">The start date of the range.</param>
        /// <param name="endDate">The end date of the range.</param>
        /// <param name="publicHolidaysList">A list of public holidays (optional). If provided, these holidays will be excluded from the business days count.</param>
        /// <param name="holidayRules">A list of holiday rules (optional). If provided, these rules will be used to calculate holidays that affect business days.</param>
        /// <returns>The number of business days between the two dates, considering weekends and holidays.</returns>
        public int BusinessDaysBetweenTwoDates(DateTime startDate, DateTime endDate, List<DateTime> publicHolidaysList = null, List<Dictionary<string, object>> holidayRules = null)
        {
            Console.WriteLine($"Calculating Business days between {startDate} and {endDate}.");

            int totalDays = 0;
            int publicHolidays = 0;

            totalDays += GetTotalDays(startDate:startDate, endDate:endDate, totalDays:totalDays);
            if (totalDays == 0){return 0;}
            
            int totalWeekendDays = _dayUtils.TotalWeekendDaysCount(startDate, totalDays);

            publicHolidays += GetHolidays(startDate: startDate, 
                                                          endDate: endDate, 
                                                          publicHolidays: publicHolidays,
                                                          publicHolidaysList: publicHolidaysList, 
                                                          holidayRules: holidayRules);

            int totalBusinessDays = totalDays - totalWeekendDays - publicHolidays;

            Console.WriteLine($"Total days: {totalDays}, Weekend days: {totalWeekendDays}, Business: {totalBusinessDays}");

            return totalBusinessDays;
        }
    
    
    
    }
}