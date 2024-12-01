using Microsoft.Extensions.Logging;



namespace design.com
{

    public class DayUtils
    {
        // private readonly ILogger<DayCounter> _logger;
        public const int numberOfDaysWeek = 7;
        public const int saturdayIndex = 5;
        public const int sundayIndex = 6;
        public HashSet<int> WeekDaysRange { get; set; }
        public HashSet<int> WeekendDaysRange { get; set; }


        public DayUtils()
        {
            // _logger = logger;
            WeekDaysRange = new HashSet<int> { 0, 1, 2, 3, 4 }; // Monday, Tuesday, Wednesday, Thursday, Friday
            WeekendDaysRange = new HashSet<int> { 5, 6 }; // Saturday, Sunday
        }

        /// <summary>
        /// Calculates the number of full days between two dates.
        /// </summary>
        /// <remarks>
        /// This method computes the difference in days between the `endDate` and the `startDate`.
        /// It subtracts 1 from the result to exclude the start date itself from the count.
        /// For example:
        /// - If `startDate` is 2024-01-01 and `endDate` is 2024-01-05, 
        ///   the difference would normally be 4 days, but the method returns 3
        ///   because the first day is excluded.
        /// </remarks>
        /// <param name="startDate">A DateTime object representing the start date.</param>
        /// <param name="endDate">A DateTime object representing the end date.</param>
        /// <returns>An integer representing the number of full days between the two dates.</returns>

        [ValidateDates]
        public static int DaysCountBetweenDates(DateTime startDate, DateTime endDate)
        {
            return (endDate - startDate).Days - 1;
        }



        /// <summary>
        /// Calculates the remainder when dividing the total number of days by the number of days in a week (7).
        /// </summary>
        /// <param name="totalDays">Total days between two dates</param>
        /// <returns>Remainder of the division</returns>
        public static int Remainder(int totalDays)
        {

            Console.WriteLine($"Calculating remainder for total_days_count_between_dates: {totalDays}");
            int remainderValue = totalDays % numberOfDaysWeek;
            Console.WriteLine($"Remainder calculated :{remainderValue}");
            return remainderValue;
        }


        /// <summary>
        /// Calculates the quotient when dividing the total number of days by the number of days in a week (7).
        /// This value represents the number of full weeks within the given date range.
        /// </summary>
        /// <param name="totalDays">Total days between two dates.</param>
        /// <returns>Returns the quotient (number of full weeks) as an integer.</returns>
        public static int Quotient(int totalDays)
        {

            Console.WriteLine($"Calculating quotient for total_days_count_between_dates: {totalDays}");
            int quotientValue = totalDays / numberOfDaysWeek;
            Console.WriteLine($"Quotient calculated:: {quotientValue}");
            return quotientValue;
        }



        /// <summary>
        /// Calculates the total number of weekend days (Saturdays and Sundays) within a given date range.
        /// </summary>
        /// <param name="startDate">The start date of the range.</param>
        /// <param name="totalDays">The total number of days between the two dates.</param>
        /// <returns>The total number of weekend days (Saturdays and Sundays) in the range.</returns>
        public int TotalWeekendDaysCount(DateTime startDate, int totalDays)
        {
            Console.WriteLine($"Calculating weekend days between {startDate} and total days count: {totalDays}");

            int remainingWeekendDays = 0;
            int remainder = Remainder(totalDays);
            int quotient = Quotient(totalDays);

            Console.WriteLine($"Remainder count: {remainder}, Quotient count: {quotient}");

            int startDateIndex = (int)startDate.DayOfWeek; // Each day has a index, such as monday 0, tuesday 1 ..

            if (remainder > 0) // which means there are extra days to check.
            {
                remainingWeekendDays += RemaningWeekendDaysCount(startDateIndex: startDateIndex, remainder: remainder, remainingWeekendDays: remainingWeekendDays);
            }

            int totalWeekendDays = quotient * 2 + remainingWeekendDays;

            Console.WriteLine($"Total weekend days : {totalWeekendDays}");

            return totalWeekendDays;
        }


        /// <summary>
        /// Calculates the number of weekend days (Saturdays and Sundays) in the remaining days
        /// after full weeks have been considered.
        /// </summary>
        /// <param name="startDateIndex">The weekday index of the start date (0 = Monday, 6 = Sunday).</param>
        /// <param name="remainder">The number of days remaining after full weeks.</param>
        /// <returns>The count of weekend days (Saturdays and Sundays) in the remaining days.</returns>
        public static int RemaningWeekendDaysCount(int startDateIndex, int remainder, int remainingWeekendDays)
        {
            Console.WriteLine($"Calculating remaining weekend days from start index: {startDateIndex} for remainder: {remainder} days");

            for (int i = 0; i <= remainder; i++)
            {
                int currentDay = (startDateIndex + i) % numberOfDaysWeek; // 6 + 0 = 6, still Sunday
                if (currentDay == saturdayIndex || currentDay == sundayIndex)
                {
                    remainingWeekendDays += 1;
                    Console.WriteLine($"Remaining weekend day detected on day {i + 1} (Index: {currentDay})");
                }
            }
            return remainingWeekendDays;
        }



        /// <summary>
        /// Calculates the total number of public holidays within the given date range.
        /// </summary>
        /// <param name="startDate">The start date of the range.</param>
        /// <param name="endDate">The end date of the range.</param>
        /// <param name="publicHolidayList">List of all possible public holidays.</param>
        /// <returns>Number of public holidays within the range.</returns>
        public int CalculatePublicHolidays(DateTime startDate, DateTime endDate, List<DateTime> publicHolidayList)
        {
            Console.WriteLine("Filtering public holidays from the generated list.");

            int publicHolidays = 0;
            foreach (var holiday in publicHolidayList)
            {
                if (WeekDaysRange.Contains((int)holiday.DayOfWeek) && holiday > startDate && holiday < endDate)
                {
                    publicHolidays += 1;
                }
            }
            return publicHolidays;
        }



        /// <summary>
        /// Generates a list of holiday dates that occur on a specific day of a month for each year in the period.
        /// </summary>
        /// <param name="startDate">The start date for the period.</param>
        /// <param name="period">The number of years for the period.</param>
        /// <param name="month">The month in which the holiday occurs.</param>
        /// <param name="day">The day of the month on which the holiday occurs.</param>
        /// <returns>A list of DateTime objects representing the generated holiday dates.</returns>
        public static List<DateTime> GeneratesDatesFrequencyForCertainPeriod(DateTime startDate, int period, int month, int day)
        {
            Console.WriteLine("Generates based dates for certain period ");

            var possibleDates = new List<DateTime>();
            for (int startYear = 0; startYear <= period; startYear++)
            {
                var holidayDate = new DateTime(startDate.Year + startYear, month, day);
                possibleDates.Add(holidayDate);
            }
            return possibleDates;
        }



        /// <summary>
        /// Filters a date by checking if it falls within the specified start and end dates.
        /// </summary>
        /// <param name="startDate">The start date of the range.</param>
        /// <param name="originalDate">The date to check.</param>
        /// <param name="endDate">The end date of the range.</param>
        /// <returns>True if the original date is within the range, otherwise false.</returns>
        public static bool FilterDate(DateTime startDate, DateTime? originalDate, DateTime endDate)
        {
            Console.WriteLine("Filtering date is in between range or not");

            if (originalDate.HasValue)
            {
                return startDate <= originalDate.Value && originalDate.Value <= endDate;
            }
            return false;
        }



        /// <summary>
        /// Generates a list of holidays that occur on a certain occurrence of a weekday within a month for each year in the period.
        /// </summary>
        /// <param name="startDate">The start date for the period.</param>
        /// <param name="period">The number of years for the period.</param>
        /// <param name="month">The month in which the holiday occurs.</param>
        /// <param name="day">The weekday of the month (e.g., Monday, Tuesday).</param>
        /// <param name="occurrence">The occurrence number (e.g., 1st, 2nd, etc.).</param>
        /// <returns>A list of DateTime objects representing the holidays that occur on the specified weekday occurrence.</returns>
        public static List<DateTime> GeneratesOccurrenceDatesFrequencyForCertainPeriod(DateTime startDate, int period, int month, int day, int occurrence)
        {

            Console.WriteLine("Generates occurence based dates for certain period ");

            var possibleHolidays = new List<DateTime>();
            for (int startYear = 0; startYear <= period; startYear++)
            {
                var firstDayOfMonth = new DateTime(startDate.Year + startYear, month, 1);
                var firstWeekdayOfMonth = (int)firstDayOfMonth.DayOfWeek;

                // Calculate the day offset to align with the desired weekday
                var dayOffset = (day - firstWeekdayOfMonth + 7) % 7;
                // Calculate the nth weekday of the month
                var nthWeekdayDate = firstDayOfMonth.AddDays(dayOffset + (occurrence - 1) * 7);
                possibleHolidays.Add(nthWeekdayDate);
            }
            return possibleHolidays;
        }


    }



}
