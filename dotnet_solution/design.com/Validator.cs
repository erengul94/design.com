using System;



namespace design.com
{

    public static class DateValidator
    {

        /// <summary>
        /// Validates the dates in the provided parameters before invoking the specified method on the given object.
        /// The method checks if the first two parameters are valid DateTime objects and ensures that the start date 
        /// is earlier than the end date, throwing an exception if invalid dates are found. If the validation passes, 
        /// the method is invoked with the provided parameters.
        ///
        /// <para>
        /// If the method specified by <paramref name="methodName"/> contains the <see cref="ValidateDatesAttribute"/> attribute, 
        /// the validation checks will be performed on the first two parameters (start date and end date).
        /// </para>
        /// <para>
        /// Throws an <see cref="ArgumentException"/> if the method is not found, if the dates are invalid, or if the parameters 
        /// do not match the expected types.
        /// </para>
        /// </summary>
        /// <param name="obj">The object on which the method is to be invoked.</param>
        /// <param name="methodName">The name of the method to be invoked on the object.</param>
        /// <param name="parameters">The parameters to be passed to the method.</param>
        /// <returns>An object representing the result of invoking the specified method, or 0 if the dates are the same.</returns>
        /// <exception cref="ArgumentException">Thrown if the method is not found, the parameters are invalid, or the date range is incorrect.</exception>

        public static object ValideteDates(object obj, string methodName, params object[] parameters)
        {
            var method = obj.GetType().GetMethod(methodName);
            if (method == null)
            {
                throw new ArgumentException("Method not found.");
            }

            var hasValidateDatesAttribute = Attribute.IsDefined(method, typeof(ValidateDatesAttribute));

            if (hasValidateDatesAttribute)
            {
                if (parameters.Length >= 2 &&
                    parameters[0] is DateTime startDate &&
                    parameters[1] is DateTime endDate)
                {
                    ValidateCalendarDate(startDate);
                    ValidateCalendarDate(endDate);

                    if (startDate > endDate)
                    {
                        throw new ArgumentException("Invalid date range: startDate must be earlier than endDate.");
                    }
                    if (startDate == endDate)
                    {
                        Console.WriteLine($"Start Date end End Date are same!");
                        return 0;
                    }

                }
                else
                {
                    throw new ArgumentException("The first two parameters must be DateTime objects.");
                }
            }

            return method.Invoke(obj, parameters);
        }

        /// <summary>
        /// Validates if the provided date is a valid calendar date. 
        /// If the date is invalid (e.g., an out-of-range date), an exception is thrown.
        ///
        /// <para>
        /// This method attempts to create a new <see cref="DateTime"/> object with the provided date, which will 
        /// throw an <see cref="ArgumentOutOfRangeException"/> if the date is not valid.
        /// </para>
        /// </summary>
        /// <param name="date">The date to be validated.</param>
        /// <exception cref="ArgumentException">Thrown if the provided date is invalid.</exception>

        private static void ValidateCalendarDate(DateTime date)
        {
            try
            {
                _ = new DateTime(date.Year, date.Month, date.Day);
            }
            catch (ArgumentOutOfRangeException ex)
            {
                throw new ArgumentException($"Invalid date Exception");
            }
        }
    }

}