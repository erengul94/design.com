// See https://aka.ms/new-console-template for more information
using System;


namespace design.com
{
    class Program
    {
        static void Main(string[] args)
        {
            DayUtils dayUtils = new DayUtils();
            BusinessDayCounter businessDayCounter = new BusinessDayCounter(dayUtils);

            //TASK1
            // DateTime startDate = new DateTime(2013, 10, 7);
            // DateTime endDate = new DateTime(2013, 10, 9);

            // DateTime startDate = new DateTime(2013, 10, 5);
            // DateTime endDate = new DateTime(2013, 10, 14);

            // DateTime startDate = new DateTime(2013, 10, 7);
            // DateTime endDate = new DateTime(2014, 1, 1);

            // int weekdays = businessDayCounter.WeekdaysBetweenTwoDates(startDate, endDate);
            // Console.WriteLine($"Weekdays between {startDate.ToShortDateString()} and {endDate.ToShortDateString()}: {weekdays}");
            // Console.WriteLine("Hello world");

            // TASK2
                DateTime firstPublicHoliday = new DateTime(2013, 12, 25);  // 25th December 2013
                DateTime secondPublicHoliday = new DateTime(2013, 12, 26); // 26th December 2013
                DateTime thirdPublicHoliday = new DateTime(2014, 1, 1);    // 1st January 2014

                // Adding the public holidays to a list
                List<DateTime> publicHolidaysList = new List<DateTime>
            {
                firstPublicHoliday,
                secondPublicHoliday,
                thirdPublicHoliday
            };
            // DateTime startDate = new DateTime(2013, 10, 7);
            // DateTime endDate = new DateTime(2013, 10, 9);

            // DateTime startDate = new DateTime(2013, 12, 24);
            // DateTime endDate = new DateTime(2013, 12, 27);

            DateTime startDate = new DateTime(2013, 10, 7);
            DateTime endDate = new DateTime(2014, 1, 1);
            int weekdays = businessDayCounter.BusinessDaysBetweenTwoDates(startDate:startDate, endDate:endDate, publicHolidaysList : publicHolidaysList);



            //TASK 3

            var holidayRules = new List<Dictionary<string, object>>
            {
                new Dictionary<string, object>
                {
                    { "holiday_type", "public_holiday" },
                    { "description", "Anzac Day" },
                    { "month", 4 },
                    { "day", 25 }
                },
                new Dictionary<string, object>
                {
                    { "holiday_type", "moveable_holiday" },
                    { "description", "New Year's Day" },
                    { "month", 1 },
                    { "day", 1 }
                },
                new Dictionary<string, object>
                {
                    { "holiday_type", "certain_occurrence_holiday" },
                    { "description", "Queen's Birthday" },
                    { "month", 6 },
                    { "day", 0 },
                    { "occurrence", 2 }
                }
            };
            // DateTime startDate = new DateTime(2013, 10, 7);
            // DateTime endDate = new DateTime(2013, 10, 9);

            // DateTime startDate = new DateTime(2013, 12, 24);
            // DateTime endDate = new DateTime(2013, 12, 27);

            // DateTime startDate = new DateTime(2013, 10, 7);
            // DateTime endDate = new DateTime(2014, 1, 1);

            // DateTime startDate = new DateTime(2023, 4, 20);
            // DateTime endDate = new DateTime(2023, 4, 26);

            // int weekdays = businessDayCounter.BusinessDaysBetweenTwoDates(startDate: startDate, endDate: endDate, holidayRules: holidayRules);


            // Console.WriteLine($"Weekdays between {startDate.ToShortDateString()} and {endDate.ToShortDateString()}: {weekdays}");
        }

    }
}
