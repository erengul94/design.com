using System.Collections.Generic;

namespace design.com
{
    class Program
    {
        static void Main(string[] args)
        {
            DayUtils dayUtils = new DayUtils();
            BusinessDayCounter businessDayCounter = new BusinessDayCounter(dayUtils);

            // Task 1: Calculate weekdays between two dates
            Task1(businessDayCounter);

            // Task 2: Calculate business days between two dates considering public holidays
            Task2(businessDayCounter);

            // Task 3: Calculate business days between two dates considering specific holiday rules
            Task3(businessDayCounter);
        }

        // Task 1: Weekdays between two dates
        static void Task1(BusinessDayCounter businessDayCounter)
        {
            try
            {
                var startEndDateList = new List<(DateTime startDate, DateTime endDate)>
                    {
                        (new DateTime(2013, 10, 7), new DateTime(2013, 10, 9)), // Result must be 1
                        (new DateTime(2013, 10, 5), new DateTime(2013, 10, 14)), // Result must be 5
                        (new DateTime(2013, 10, 7), new DateTime(2014, 1, 1)),  // Result must be 61
                        (new DateTime(2013, 10, 5), new DateTime(2013, 10, 7))  // Result must be 0
                    };
                Console.WriteLine(new string('=', 50));
                Console.WriteLine("Task 1: Week Days");
                Console.WriteLine(new string('=', 50));

                foreach (var (startDate, endDate) in startEndDateList)
                {
                    int weekdays = businessDayCounter.WeekdaysBetweenTwoDates(startDate, endDate);
                    Console.WriteLine(new string('-', 50));
                    Console.WriteLine($"Start Date : {startDate.ToShortDateString()}");
                    Console.WriteLine($"End Date   : {endDate.ToShortDateString()}");
                    Console.WriteLine($"Week Days (Excluding Holidays): {weekdays}");
                    Console.WriteLine(new string('-', 50));
                }

            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                Environment.Exit(1); // This stops the application with an error code.
            }

        }

        // Task 2: Business days between two dates considering public holidays
        static void Task2(BusinessDayCounter businessDayCounter)
        {

            try
            {
                // Define the list of public holidays
                List<DateTime> publicHolidaysList = new List<DateTime>
                {
                    new DateTime(2013, 12, 25),  // 25th December 2013
                    new DateTime(2013, 12, 26), // 26th December 2013
                    new DateTime(2014, 1, 1)    // 1st January 2014
                };


                // Define a list of start and end dates
                var startEndDateList = new List<(DateTime startDate, DateTime endDate)>
                {
                    (new DateTime(2013, 10, 7), new DateTime(2013, 10, 9)), // Result must be 1
                    (new DateTime(2013, 12, 24), new DateTime(2013, 12, 27)), // Result must be 0
                    (new DateTime(2013, 10, 7), new DateTime(2014, 1, 1))  // Result must be 59
                };

                Console.WriteLine(new string('=', 50)); // Separator line
                Console.WriteLine("Task 2: Business Days with Holiday List of Holidays");
                Console.WriteLine(new string('=', 50));

                foreach (var (startDate, endDate) in startEndDateList)
                {
                    int businessDays = businessDayCounter.BusinessDaysBetweenTwoDates(startDate: startDate, endDate: endDate, publicHolidaysList: publicHolidaysList);
                    Console.WriteLine(new string('-', 50));
                    Console.WriteLine($"Start Date : {startDate.ToShortDateString()}");
                    Console.WriteLine($"End Date   : {endDate.ToShortDateString()}");
                    Console.WriteLine($"Business Days (Excluding Holidays): {businessDays}");
                    Console.WriteLine(new string('-', 50));
                }

            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                Environment.Exit(1); // This stops the application with an error code.

            }

        }

        // Task 3: Business days between two dates considering specific holiday rules
        static void Task3(BusinessDayCounter businessDayCounter)
        {
            // Define the holiday rules
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

            
            try
            {
                var startEndDateList = new List<(DateTime startDate, DateTime endDate)>
                {
                    (new DateTime(2022, 12, 26), new DateTime(2023, 1, 3)), // Result must be 4 # "New Year's Day case"
                    (new DateTime(2023, 4, 20), new DateTime(2023, 4, 27)), //Result must be 3 # for "Anzac Day case"
                    (new DateTime(2023, 6, 9), new DateTime(2023, 6, 15)) //Result must be 2 # for  "Queen's Birthday case"
                };

                Console.WriteLine(new string('=', 50));
                Console.WriteLine("Task 3: Business Days with Holiday Rules");
                Console.WriteLine(new string('=', 50));

                foreach (var (startDate, endDate) in startEndDateList)
                {
                    int businessDays = businessDayCounter.BusinessDaysBetweenTwoDates(startDate: startDate, endDate: endDate, holidayRules: holidayRules);

                    Console.WriteLine(new string('-', 50));
                    Console.WriteLine($"Start Date : {startDate.ToShortDateString()}");
                    Console.WriteLine($"End Date   : {endDate.ToShortDateString()}");
                    Console.WriteLine($"Business Days (Excluding Holidays): {businessDays}");
                    Console.WriteLine(new string('-', 50));
                }

            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                Environment.Exit(1);
            }

        }

    }
}


