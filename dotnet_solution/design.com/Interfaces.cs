// public interface IAppLogger<T>
// {
//     void LogInformation(string message);
//     void LogWarning(string message);
//     void LogError(string message, Exception exception = null);
//     void LogDebug(string message);
// }


namespace design.com
{
    public interface IHolidayFactoryInterface
    {
        List<DateTime> GetHoliday();
        bool CheckHolidayRule(Dictionary<string, object> holidayRule); 

        List<DateTime> GenerateDates(Dictionary<string, object> holidayRule);
    }
}