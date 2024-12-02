// public interface IAppLogger<T>
// {
//     void LogInformation(string message);
//     void LogWarning(string message);
//     void LogError(string message, Exception exception = null);
//     void LogDebug(string message);
// }


namespace design.com
{
/// <summary>
/// Interface for holiday factory classes that define various types of holidays.
/// Provides methods to retrieve holidays, validate holiday rules, and generate holiday dates.
/// </summary>
public interface IHolidayFactoryInterface
{
    /// <summary>
    /// Retrieves the list of holiday dates based on the specific holiday type and rules.
    /// </summary>
    /// <returns>A list of DateTime objects representing the holiday dates.</returns>
    List<DateTime> GetHoliday();

    /// <summary>
    /// Validates the given holiday rule to ensure it contains the necessary information.
    /// </summary>
    /// <param name="holidayRule">A dictionary containing the holiday rule data.</param>
    /// <returns>True if the holiday rule is valid; otherwise, throws an exception.</returns>
    bool CheckHolidayRule(Dictionary<string, object> holidayRule);

    /// <summary>
    /// Generates the holiday dates based on the holiday rule for a specific period.
    /// </summary>
    /// <param name="holidayRule">A dictionary containing the holiday rule data.</param>
    /// <returns>A list of DateTime objects representing the generated holiday dates.</returns>
    List<DateTime> GenerateDates(Dictionary<string, object> holidayRule);
}

}