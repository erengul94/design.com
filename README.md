# Project Name

### . Need Help?

**In case the instructions are not enough or cannot be followed as explained, feel free to reach me!**

1. [My Approach and Architecture of the Project](#1-my-approach-and-architecture-of-the-project)
2. [How Can I Run the Projects?](#2-how-can-i-run-the-projects)
    - 2.1. [Python](#21-Python)  
    - 2.2. [Dotnet](#22-Dotnet)
3. [How Can I Run the Unittests?](#3-how-can-i-run-the-unittests)
4. [Code Documentation](#4-code-documentation)
    - 4.1. [Python](#41-python)  
    - 4.2. [Dotnet](#42-dotnet)
5. [TODO's](#5-todos)

## 1. My Approach and Architecture of the Project

In this project, I used a modular approach to design a flexible and scalable system. The architecture focuses on clean separation of concerns in both Python and .NET. In .Net part, I've tried my best to code it up and follow the guidelines. So, if you spot something that looks a little off, please consider it a learning opportunity in 4-5 days :). 

The core idea is to handle holiday rules and the generation of holiday dates for various scenarios, such as public holidays, moveable holidays, and certain occurrence holidays.

Key features of the architecture:


### **Factory**
The Factory pattern is centralized in services such as `HolidayFactory` and its associated holiday classes. This pattern provides scalability by enabling the creation of different types of holiday instances easily. Once new types of holidays are added to the system, they can be created simply by introducing a new class. This modular approach ensures that the system remains flexible and extensible as it grows.

- **Scalability**: Adding new holiday types is straightforward by creating a new class.
- **Centralization**: The `HolidayFactory` centralizes the holiday creation logic, simplifying maintenance.

### **Validator**
The `ValideteDates` method ensures that date inputs are valid and conform to the expected format and range. It plays a critical role in maintaining data integrity by verifying that dates are correctly formatted and fall within a valid range. The `DateValidator` uses generic methods that can be applied to various functions, taking in parameters such as `startDate` and `endDate`, and validating that the date values are properly structured.

- **Validation**: Ensures that dates follow correct formats and ranges.
- **Reusability**: The methods in `ValideteDates` are generic and can be used across various functions requiring date validation.
- **Data Integrity**: Maintains the integrity of the system by preventing invalid dates from being processed.

### **DayUtils Class**

The `DayUtils` class provides utility methods for handling date manipulations, focusing on calculating the number of days between two dates, determining weekend days, calculating public holidays, and generating holiday dates within a specified period. It is ideal for use in applications where date-related calculations and date filtering are needed.


## 2. How Can I Run the Projects?

### 2.1. Python

```markdown

To run the Python project, follow these steps:

#### 1. Install Python

Make sure Python 3.x is installed on your system. If you don’t have Python installed, follow these steps:

- **Windows**: Download Python from the [official Python website](https://www.python.org/downloads/). During installation, make sure to check the box that says "Add Python to PATH".
- **macOS**: Python 3 is usually pre-installed. You can verify this by running:
    ```bash
    python3 --version
    ```
    If it is not installed, you can install it via Homebrew:
    ```bash
    brew install python
    ```
- **Linux**: Use your package manager to install Python:
    - For Ubuntu/Debian-based systems:
      ```bash
      sudo apt update
      sudo apt install python3 python3-pip
      ```
    - For Fedora:
      ```bash
      sudo dnf install python3 python3-pip
      ```

Once Python is installed, verify the installation by running:
```bash
python --version
```
or if `python3` is the default:
```bash
python3 --version
```

Here's the updated `README.md` file with the section on setting up the project environment and including the `requirements.txt` part:

---

### 2. Set Up the Project Environment

1. **Clone or Download the Project**: Download or clone the project repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/design.com.git
    ```

2. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the project folder:

    ```bash
    cd ~/design.com/python_solution
    ```

3. **Set Up a Virtual Environment**: It's recommended to use a virtual environment to manage dependencies. Create and activate one using the following commands:

    ```bash
    # Create a virtual environment
    python3 -m venv venv

    # Activate the virtual environment
    # For macOS/Linux
    source venv/bin/activate

    # For Windows
    .\venv\Scripts\activate
    ```

4. **Install Project Dependencies**: The required dependencies are listed in the `requirements.txt` file. Install them by running:

    ```bash
    pip install -r requirements.txt
    ```


---


#### 3. Running the Python Scripts

If you want to run multiple Python scripts (e.g., task-specific scripts), you can execute them like so:

- **Run Task 1**:
    ```bash
    python3 python_solution_task1.py
    ```
- **Output Of Task 1**:
```
2024-12-03 00:30:01,988 - INFO - ==================================================
2024-12-03 00:30:01,988 - INFO - Running Task 1: Weekdays Between Two Dates
2024-12-03 00:30:01,988 - INFO - ==================================================
2024-12-03 00:30:01,988 - INFO - Start date: 2013-10-07, End date: 2013-10-09
2024-12-03 00:30:01,988 - INFO - Calculating weekdays between 2013-10-07 and 2013-10-09.
2024-12-03 00:30:01,988 - INFO - Validating dates: start_date=2013-10-07, end_date=2013-10-09
2024-12-03 00:30:01,988 - INFO - Result after validation: 1
2024-12-03 00:30:01,988 - INFO - Calculating weekend days between 2013-10-07 and total days count: 1
2024-12-03 00:30:01,988 - INFO - Calculating remainder for total_days_count_between_dates: 1
2024-12-03 00:30:01,988 - INFO - Remainder calculated: 1
2024-12-03 00:30:01,988 - INFO - Calculating quotient for total_days_count_between_dates: 1
2024-12-03 00:30:01,988 - INFO - Quotient calculated: 0
2024-12-03 00:30:01,988 - INFO - Remainder count: 1, Quotient count: 0
2024-12-03 00:30:01,988 - INFO - Calculating remaining weekend days from start index: 0 for remainder: 1 days
2024-12-03 00:30:01,988 - INFO - Total remaining weekend days: 0
2024-12-03 00:30:01,988 - INFO - Total weekend days: 0
2024-12-03 00:30:01,988 - INFO - Total days: 1, Weekend days: 0, Weekdays: 1
2024-12-03 00:30:01,988 - INFO - ==================================================
2024-12-03 00:30:01,988 - INFO - Start Date: 2013-10-07
2024-12-03 00:30:01,988 - INFO - End Date  : 2013-10-09
2024-12-03 00:30:01,988 - INFO - Weekdays  : 1
2024-12-03 00:30:01,988 - INFO - ==================================================
2024-12-03 00:30:01,988 - INFO - ==================================================
2024-12-03 00:30:01,989 - INFO - Running Task 1: Weekdays Between Two Dates
2024-12-03 00:30:01,989 - INFO - ==================================================
2024-12-03 00:30:01,989 - INFO - Start date: 2013-10-05, End date: 2013-10-14
2024-12-03 00:30:01,989 - INFO - Calculating weekdays between 2013-10-05 and 2013-10-14.
2024-12-03 00:30:01,989 - INFO - Validating dates: start_date=2013-10-05, end_date=2013-10-14
2024-12-03 00:30:01,989 - INFO - Result after validation: 8
2024-12-03 00:30:01,989 - INFO - Calculating weekend days between 2013-10-05 and total days count: 8
2024-12-03 00:30:01,989 - INFO - Calculating remainder for total_days_count_between_dates: 8
2024-12-03 00:30:01,989 - INFO - Remainder calculated: 1
2024-12-03 00:30:01,989 - INFO - Calculating quotient for total_days_count_between_dates: 8
2024-12-03 00:30:01,989 - INFO - Quotient calculated: 1
2024-12-03 00:30:01,989 - INFO - Remainder count: 1, Quotient count: 1
2024-12-03 00:30:01,989 - INFO - Calculating remaining weekend days from start index: 5 for remainder: 1 days
2024-12-03 00:30:01,989 - INFO - Remaining weekend day detected on day 2 (Index: 6)
2024-12-03 00:30:01,989 - INFO - Total remaining weekend days: 1
2024-12-03 00:30:01,989 - INFO - Total weekend days: 3
2024-12-03 00:30:01,989 - INFO - Total days: 8, Weekend days: 3, Weekdays: 5
2024-12-03 00:30:01,989 - INFO - ==================================================
2024-12-03 00:30:01,989 - INFO - Start Date: 2013-10-05
2024-12-03 00:30:01,989 - INFO - End Date  : 2013-10-14
2024-12-03 00:30:01,989 - INFO - Weekdays  : 5
2024-12-03 00:30:01,989 - INFO - ==================================================
2024-12-03 00:30:01,989 - INFO - ==================================================
2024-12-03 00:30:01,989 - INFO - Running Task 1: Weekdays Between Two Dates
2024-12-03 00:30:01,989 - INFO - ==================================================
2024-12-03 00:30:01,989 - INFO - Start date: 2013-10-07, End date: 2014-01-01
2024-12-03 00:30:01,989 - INFO - Calculating weekdays between 2013-10-07 and 2014-01-01.
2024-12-03 00:30:01,989 - INFO - Validating dates: start_date=2013-10-07, end_date=2014-01-01
2024-12-03 00:30:01,989 - INFO - Result after validation: 85
2024-12-03 00:30:01,989 - INFO - Calculating weekend days between 2013-10-07 and total days count: 85
2024-12-03 00:30:01,989 - INFO - Calculating remainder for total_days_count_between_dates: 85
2024-12-03 00:30:01,989 - INFO - Remainder calculated: 1
2024-12-03 00:30:01,989 - INFO - Calculating quotient for total_days_count_between_dates: 85
2024-12-03 00:30:01,989 - INFO - Quotient calculated: 12
2024-12-03 00:30:01,990 - INFO - Remainder count: 1, Quotient count: 12
2024-12-03 00:30:01,990 - INFO - Calculating remaining weekend days from start index: 0 for remainder: 1 days
2024-12-03 00:30:01,990 - INFO - Total remaining weekend days: 0
2024-12-03 00:30:01,990 - INFO - Total weekend days: 24
2024-12-03 00:30:01,990 - INFO - Total days: 85, Weekend days: 24, Weekdays: 61
2024-12-03 00:30:01,990 - INFO - ==================================================
2024-12-03 00:30:01,990 - INFO - Start Date: 2013-10-07
2024-12-03 00:30:01,990 - INFO - End Date  : 2014-01-01
2024-12-03 00:30:01,990 - INFO - Weekdays  : 61
2024-12-03 00:30:01,990 - INFO - ==================================================
2024-12-03 00:30:01,990 - INFO - ==================================================
2024-12-03 00:30:01,990 - INFO - Running Task 1: Weekdays Between Two Dates
2024-12-03 00:30:01,990 - INFO - ==================================================
2024-12-03 00:30:01,990 - INFO - Start date: 2013-10-07, End date: 2013-10-05
2024-12-03 00:30:01,990 - INFO - Calculating weekdays between 2013-10-07 and 2013-10-05.
2024-12-03 00:30:01,990 - INFO - Validating dates: start_date=2013-10-07, end_date=2013-10-05
2024-12-03 00:30:01,990 - WARNING - Invalid date range: start_date >= end_date. Returning 0.
2024-12-03 00:30:01,990 - INFO - ==================================================
2024-12-03 00:30:01,990 - INFO - Start Date: 2013-10-07
2024-12-03 00:30:01,990 - INFO - End Date  : 2013-10-05
2024-12-03 00:30:01,990 - INFO - Weekdays  : 0
2024-12-03 00:30:01,990 - INFO - ==================================================
```

---

**Note**: 

- If you want to edit the date range in Task 1, you can easily change the `datetime` objects within the `start_end_date_list` list.  
- **For Example**:  
    The following:  
    ```python
    "start_date": datetime.date(2013, 10, 7),
    "end_date": datetime.date(2013, 10, 9)
    ```  
    Can be changed to:  
    ```python
    "start_date": datetime.date(2013, 1, 10),
    "end_date": datetime.date(2013, 12, 9)
    ```

---



- **Run Task 2**:
    ```bash
    python3 python_solution_task2.py
    ```

- **Output Of Task 2**:

 ```
2024-12-03 00:33:33,808 - INFO - ==================================================
2024-12-03 00:33:33,808 - INFO - Running Task 2: Business Days Between Two Dates
2024-12-03 00:33:33,808 - INFO - ==================================================
2024-12-03 00:33:33,808 - INFO - Start date: 2013-10-07, End date: 2013-10-09
2024-12-03 00:33:33,808 - INFO - Business days between 2013-10-07 and 2013-10-09.
2024-12-03 00:33:33,808 - INFO - Validating dates: start_date=2013-10-07, end_date=2013-10-09
2024-12-03 00:33:33,808 - INFO - Result after validation: 1
2024-12-03 00:33:33,808 - INFO - Calculating weekend days between 2013-10-07 and total days count: 1
2024-12-03 00:33:33,808 - INFO - Calculating remainder for total_days_count_between_dates: 1
2024-12-03 00:33:33,808 - INFO - Remainder calculated: 1
2024-12-03 00:33:33,808 - INFO - Calculating quotient for total_days_count_between_dates: 1
2024-12-03 00:33:33,808 - INFO - Quotient calculated: 0
2024-12-03 00:33:33,808 - INFO - Remainder count: 1, Quotient count: 0
2024-12-03 00:33:33,808 - INFO - Calculating remaining weekend days from start index: 0 for remainder: 1 days
2024-12-03 00:33:33,809 - INFO - Total remaining weekend days: 0
2024-12-03 00:33:33,809 - INFO - Total weekend days: 0
2024-12-03 00:33:33,809 - INFO - Filtering public holidays from the generated list.
2024-12-03 00:33:33,809 - INFO - Total days: 1, Weekend days: 0, Business: 1
2024-12-03 00:33:33,809 - INFO - ==================================================
2024-12-03 00:33:33,809 - INFO - Start Date: 2013-10-07
2024-12-03 00:33:33,809 - INFO - End Date  : 2013-10-09
2024-12-03 00:33:33,809 - INFO - Business Days  : 1
2024-12-03 00:33:33,809 - INFO - ==================================================
2024-12-03 00:33:33,809 - INFO - ==================================================
2024-12-03 00:33:33,809 - INFO - Running Task 2: Business Days Between Two Dates
2024-12-03 00:33:33,809 - INFO - ==================================================
2024-12-03 00:33:33,809 - INFO - Start date: 2013-12-24, End date: 2013-12-27
2024-12-03 00:33:33,809 - INFO - Business days between 2013-12-24 and 2013-12-27.
2024-12-03 00:33:33,809 - INFO - Validating dates: start_date=2013-12-24, end_date=2013-12-27
2024-12-03 00:33:33,809 - INFO - Result after validation: 2
2024-12-03 00:33:33,809 - INFO - Calculating weekend days between 2013-12-24 and total days count: 2
2024-12-03 00:33:33,809 - INFO - Calculating remainder for total_days_count_between_dates: 2
2024-12-03 00:33:33,809 - INFO - Remainder calculated: 2
2024-12-03 00:33:33,809 - INFO - Calculating quotient for total_days_count_between_dates: 2
2024-12-03 00:33:33,809 - INFO - Quotient calculated: 0
2024-12-03 00:33:33,809 - INFO - Remainder count: 2, Quotient count: 0
2024-12-03 00:33:33,809 - INFO - Calculating remaining weekend days from start index: 1 for remainder: 2 days
2024-12-03 00:33:33,809 - INFO - Total remaining weekend days: 0
2024-12-03 00:33:33,809 - INFO - Total weekend days: 0
2024-12-03 00:33:33,809 - INFO - Filtering public holidays from the generated list.
2024-12-03 00:33:33,809 - INFO - Total days: 2, Weekend days: 0, Business: 0
2024-12-03 00:33:33,809 - INFO - ==================================================
2024-12-03 00:33:33,809 - INFO - Start Date: 2013-12-24
2024-12-03 00:33:33,809 - INFO - End Date  : 2013-12-27
2024-12-03 00:33:33,809 - INFO - Business Days  : 0
2024-12-03 00:33:33,809 - INFO - ==================================================
2024-12-03 00:33:33,809 - INFO - ==================================================
2024-12-03 00:33:33,809 - INFO - Running Task 2: Business Days Between Two Dates
2024-12-03 00:33:33,809 - INFO - ==================================================
2024-12-03 00:33:33,810 - INFO - Start date: 2013-10-07, End date: 2014-01-01
2024-12-03 00:33:33,810 - INFO - Business days between 2013-10-07 and 2014-01-01.
2024-12-03 00:33:33,810 - INFO - Validating dates: start_date=2013-10-07, end_date=2014-01-01
2024-12-03 00:33:33,810 - INFO - Result after validation: 85
2024-12-03 00:33:33,810 - INFO - Calculating weekend days between 2013-10-07 and total days count: 85
2024-12-03 00:33:33,810 - INFO - Calculating remainder for total_days_count_between_dates: 85
2024-12-03 00:33:33,810 - INFO - Remainder calculated: 1
2024-12-03 00:33:33,810 - INFO - Calculating quotient for total_days_count_between_dates: 85
2024-12-03 00:33:33,810 - INFO - Quotient calculated: 12
2024-12-03 00:33:33,810 - INFO - Remainder count: 1, Quotient count: 12
2024-12-03 00:33:33,810 - INFO - Calculating remaining weekend days from start index: 0 for remainder: 1 days
2024-12-03 00:33:33,810 - INFO - Total remaining weekend days: 0
2024-12-03 00:33:33,810 - INFO - Total weekend days: 24
2024-12-03 00:33:33,810 - INFO - Filtering public holidays from the generated list.
2024-12-03 00:33:33,810 - INFO - Total days: 85, Weekend days: 24, Business: 59
2024-12-03 00:33:33,810 - INFO - ==================================================
2024-12-03 00:33:33,810 - INFO - Start Date: 2013-10-07
2024-12-03 00:33:33,810 - INFO - End Date  : 2014-01-01
2024-12-03 00:33:33,810 - INFO - Business Days  : 59
2024-12-03 00:33:33,810 - INFO - ==================================================

```

**Note**: 

- If you want to edit the date range in Task 2, you can easily change the `datetime` objects within the `start_end_date_list` list.  
- **For Example**:  
    The following:  
    ```python
    {
    "start_date": datetime.date(2013, 10, 7),
    "end_date": datetime.date(2013, 10, 9)}
    ```  
    Can be changed to:  
    ```python
    {
    "start_date": datetime.date(2013, 1, 10),
    "end_date": datetime.date(2013, 12, 9)}
    ```

- If you want to add or remove public holiday in Task 2
- **For Example**:  
    The following:  
    ```python
        first_public_holiday = datetime.date(2013, 12, 25)
        public_holiday_list = [
            first_public_holiday,
            second_public_holiday,
            third_public_holiday
        ]

    ```  
    Can be changed to:  
    ```python
        new_public_holiday = datetime.date(2013, 12, 1)
        public_holiday_list = [
            first_public_holiday,
            second_public_holiday,
            third_public_holiday,
            new_public_holiday
        ]
    ```

---


- **Run Task 3**:
    ```bash
    python3 python_solution_task3.py
    ```
- **Output Of Task 1**:

```
/Users/erengul/Documents/venvs/orchestrator-venv/bin/python3.8 /Users/erengul/Documents/projects/design.com/python_solution/task3.py 
2024-12-03 00:37:46,477 - INFO - ==================================================
2024-12-03 00:37:46,477 - INFO - Running Task 2: Business Days Between Two Dates
2024-12-03 00:37:46,477 - INFO - ==================================================
2024-12-03 00:37:46,477 - INFO - Start date: 2022-12-26, End date: 2023-01-03
2024-12-03 00:37:46,478 - INFO - Business days between 2022-12-26 and 2023-01-03.
2024-12-03 00:37:46,478 - INFO - Validating dates: start_date=2022-12-26, end_date=2023-01-03
2024-12-03 00:37:46,478 - INFO - Result after validation: 7
2024-12-03 00:37:46,478 - INFO - Calculating weekend days between 2022-12-26 and total days count: 7
2024-12-03 00:37:46,478 - INFO - Calculating remainder for total_days_count_between_dates: 7
2024-12-03 00:37:46,478 - INFO - Remainder calculated: 0
2024-12-03 00:37:46,478 - INFO - Calculating quotient for total_days_count_between_dates: 7
2024-12-03 00:37:46,478 - INFO - Quotient calculated: 1
2024-12-03 00:37:46,478 - INFO - Remainder count: 0, Quotient count: 1
2024-12-03 00:37:46,478 - INFO - Total weekend days: 2
2024-12-03 00:37:46,478 - INFO - Holiday 2022-01-01 is a Saturday. Moved to Monday: 2022-01-03
2024-12-03 00:37:46,478 - INFO - Holiday 2023-01-01 is a Sunday. Moved to Monday: 2023-01-02
2024-12-03 00:37:46,478 - INFO - Filtering public holidays from the generated list.
2024-12-03 00:37:46,478 - INFO - Total days: 7, Weekend days: 2, Business: 4
2024-12-03 00:37:46,478 - INFO - ==================================================
2024-12-03 00:37:46,478 - INFO - Start Date: 2022-12-26
2024-12-03 00:37:46,478 - INFO - End Date  : 2023-01-03
2024-12-03 00:37:46,478 - INFO - Business Days  : 4
2024-12-03 00:37:46,478 - INFO - ==================================================
2024-12-03 00:37:46,478 - INFO - ==================================================
2024-12-03 00:37:46,478 - INFO - Running Task 2: Business Days Between Two Dates
2024-12-03 00:37:46,478 - INFO - ==================================================
2024-12-03 00:37:46,478 - INFO - Start date: 2023-04-20, End date: 2023-04-27
2024-12-03 00:37:46,478 - INFO - Business days between 2023-04-20 and 2023-04-27.
2024-12-03 00:37:46,478 - INFO - Validating dates: start_date=2023-04-20, end_date=2023-04-27
2024-12-03 00:37:46,479 - INFO - Result after validation: 6
2024-12-03 00:37:46,479 - INFO - Calculating weekend days between 2023-04-20 and total days count: 6
2024-12-03 00:37:46,479 - INFO - Calculating remainder for total_days_count_between_dates: 6
2024-12-03 00:37:46,479 - INFO - Remainder calculated: 6
2024-12-03 00:37:46,479 - INFO - Calculating quotient for total_days_count_between_dates: 6
2024-12-03 00:37:46,479 - INFO - Quotient calculated: 0
2024-12-03 00:37:46,479 - INFO - Remainder count: 6, Quotient count: 0
2024-12-03 00:37:46,479 - INFO - Calculating remaining weekend days from start index: 3 for remainder: 6 days
2024-12-03 00:37:46,479 - INFO - Remaining weekend day detected on day 3 (Index: 5)
2024-12-03 00:37:46,479 - INFO - Remaining weekend day detected on day 4 (Index: 6)
2024-12-03 00:37:46,479 - INFO - Total remaining weekend days: 2
2024-12-03 00:37:46,479 - INFO - Total weekend days: 2
2024-12-03 00:37:46,479 - INFO - Holiday 2023-01-01 is a Sunday. Moved to Monday: 2023-01-02
2024-12-03 00:37:46,479 - INFO - Filtering public holidays from the generated list.
2024-12-03 00:37:46,479 - INFO - Total days: 6, Weekend days: 2, Business: 3
2024-12-03 00:37:46,479 - INFO - ==================================================
2024-12-03 00:37:46,479 - INFO - Start Date: 2023-04-20
2024-12-03 00:37:46,479 - INFO - End Date  : 2023-04-27
2024-12-03 00:37:46,479 - INFO - Business Days  : 3
2024-12-03 00:37:46,479 - INFO - ==================================================
2024-12-03 00:37:46,479 - INFO - ==================================================
2024-12-03 00:37:46,479 - INFO - Running Task 2: Business Days Between Two Dates
2024-12-03 00:37:46,479 - INFO - ==================================================
2024-12-03 00:37:46,479 - INFO - Start date: 2023-06-09, End date: 2023-06-15
2024-12-03 00:37:46,479 - INFO - Business days between 2023-06-09 and 2023-06-15.
2024-12-03 00:37:46,479 - INFO - Validating dates: start_date=2023-06-09, end_date=2023-06-15
2024-12-03 00:37:46,479 - INFO - Result after validation: 5
2024-12-03 00:37:46,479 - INFO - Calculating weekend days between 2023-06-09 and total days count: 5
2024-12-03 00:37:46,479 - INFO - Calculating remainder for total_days_count_between_dates: 5
2024-12-03 00:37:46,479 - INFO - Remainder calculated: 5
2024-12-03 00:37:46,479 - INFO - Calculating quotient for total_days_count_between_dates: 5
2024-12-03 00:37:46,479 - INFO - Quotient calculated: 0
2024-12-03 00:37:46,479 - INFO - Remainder count: 5, Quotient count: 0
2024-12-03 00:37:46,479 - INFO - Calculating remaining weekend days from start index: 4 for remainder: 5 days
2024-12-03 00:37:46,479 - INFO - Remaining weekend day detected on day 2 (Index: 5)
2024-12-03 00:37:46,479 - INFO - Remaining weekend day detected on day 3 (Index: 6)
2024-12-03 00:37:46,479 - INFO - Total remaining weekend days: 2
2024-12-03 00:37:46,479 - INFO - Total weekend days: 2
2024-12-03 00:37:46,479 - INFO - Holiday 2023-01-01 is a Sunday. Moved to Monday: 2023-01-02
2024-12-03 00:37:46,480 - INFO - Filtering public holidays from the generated list.
2024-12-03 00:37:46,480 - INFO - Total days: 5, Weekend days: 2, Business: 2
2024-12-03 00:37:46,480 - INFO - ==================================================
2024-12-03 00:37:46,480 - INFO - Start Date: 2023-06-09
2024-12-03 00:37:46,480 - INFO - End Date  : 2023-06-15
2024-12-03 00:37:46,480 - INFO - Business Days  : 2
2024-12-03 00:37:46,480 - INFO - ==================================================

 ```
---
**Note**

- If you want to add or remove public holiday rule in Task 3
- **For Example**:  
    The following:  
    ```python
     holiday_rules = [
        {
            "holiday_type": "public_holiday",
             "description": "Anzac Day",
             "month": 4,
             "day": 25
         },

        {
            "holiday_type": "moveable_holiday",
            "description": "New Year's Day",
            "month": 1,
            "day": 1},
        {
            "holiday_type": "certain_occurrence_holiday",
            "description": "Queen's Birthday",
            "month": 6,
            "day": 0,
            "occurrence": 2
        }
    ]

    ```  
    Can be changed to:  
    ```python
             holiday_rules = [
        {
            "holiday_type": "public_holiday",
             "description": "Happy Software Engineering day",
             "month": 3,
             "day": 10
         },
        {
            "holiday_type": "public_holiday",
             "description": "Anzac Day",
             "month": 4,
             "day": 25
         },

        {
            "holiday_type": "moveable_holiday",
            "description": "New Year's Day",
            "month": 1,
            "day": 1},
        {
            "holiday_type": "certain_occurrence_holiday",
            "description": "Queen's Birthday",
            "month": 6,
            "day": 0,
            "occurrence": 2
        }
    ]
    ```

---


 
#### 4. Running the all tasks at once 

```bash
./run_all_task.sh
```


---



### 2.2. Dotnet

To run the .NET project, you can run all there tasks at once by just running Program.cs file. ( I think you know more than me :) )
Just please make sure Microsoft.Extensions.Logging file is installed incase is not built in.


- **Output Of Task 1, 2, 3**:

```
==================================================
Task 1: Week Days
==================================================
Calculating weekdays between 7.10.2013 00:00:00 and 9.10.2013 00:00:00.
Calculating weekend days between 7.10.2013 00:00:00 and total days count: 1
Calculating remainder for total_days_count_between_dates: 1
Remainder calculated :1
Calculating quotient for total_days_count_between_dates: 1
Quotient calculated:: 0
Remainder count: 1, Quotient count: 0
Calculating remaining weekend days from start index: 1 for remainder: 1 days
Total weekend days : 0
Total days: 1, Weekend days: 0, Weekdays: 1
--------------------------------------------------
Start Date : 7.10.2013
End Date   : 9.10.2013
Week Days (Excluding Holidays): 1
--------------------------------------------------
Calculating weekdays between 5.10.2013 00:00:00 and 14.10.2013 00:00:00.
Calculating weekend days between 5.10.2013 00:00:00 and total days count: 8
Calculating remainder for total_days_count_between_dates: 8
Remainder calculated :1
Calculating quotient for total_days_count_between_dates: 8
Quotient calculated:: 1
Remainder count: 1, Quotient count: 1
Calculating remaining weekend days from start index: 6 for remainder: 1 days
Remaining weekend day detected on day 1 (Index: 6)
Total weekend days : 3
Total days: 8, Weekend days: 3, Weekdays: 5
--------------------------------------------------
Start Date : 5.10.2013
End Date   : 14.10.2013
Week Days (Excluding Holidays): 5
--------------------------------------------------
Calculating weekdays between 7.10.2013 00:00:00 and 1.01.2014 00:00:00.
Calculating weekend days between 7.10.2013 00:00:00 and total days count: 85
Calculating remainder for total_days_count_between_dates: 85
Remainder calculated :1
Calculating quotient for total_days_count_between_dates: 85
Quotient calculated:: 12
Remainder count: 1, Quotient count: 12
Calculating remaining weekend days from start index: 1 for remainder: 1 days
Total weekend days : 24
Total days: 85, Weekend days: 24, Weekdays: 61
--------------------------------------------------
Start Date : 7.10.2013
End Date   : 1.01.2014
Week Days (Excluding Holidays): 61
--------------------------------------------------
Calculating weekdays between 5.10.2013 00:00:00 and 7.10.2013 00:00:00.
Calculating weekend days between 5.10.2013 00:00:00 and total days count: 1
Calculating remainder for total_days_count_between_dates: 1
Remainder calculated :1
Calculating quotient for total_days_count_between_dates: 1
Quotient calculated:: 0
Remainder count: 1, Quotient count: 0
Calculating remaining weekend days from start index: 6 for remainder: 1 days
Remaining weekend day detected on day 1 (Index: 6)
Total weekend days : 1
Total days: 1, Weekend days: 1, Weekdays: 0
--------------------------------------------------
Start Date : 5.10.2013
End Date   : 7.10.2013
Week Days (Excluding Holidays): 0
--------------------------------------------------
==================================================
Task 2: Business Days with Holiday List of Holidays
==================================================
Calculating Business days between 7.10.2013 00:00:00 and 9.10.2013 00:00:00.
Calculating weekend days between 7.10.2013 00:00:00 and total days count: 1
Calculating remainder for total_days_count_between_dates: 1
Remainder calculated :1
Calculating quotient for total_days_count_between_dates: 1
Quotient calculated:: 0
Remainder count: 1, Quotient count: 0
Calculating remaining weekend days from start index: 1 for remainder: 1 days
Total weekend days : 0
Filtering public holidays from the generated list.
Total days: 1, Weekend days: 0, Business: 1
--------------------------------------------------
Start Date : 7.10.2013
End Date   : 9.10.2013
Business Days (Excluding Holidays): 1
--------------------------------------------------
Calculating Business days between 24.12.2013 00:00:00 and 27.12.2013 00:00:00.
Calculating weekend days between 24.12.2013 00:00:00 and total days count: 2
Calculating remainder for total_days_count_between_dates: 2
Remainder calculated :2
Calculating quotient for total_days_count_between_dates: 2
Quotient calculated:: 0
Remainder count: 2, Quotient count: 0
Calculating remaining weekend days from start index: 2 for remainder: 2 days
Total weekend days : 0
Filtering public holidays from the generated list.
Total days: 2, Weekend days: 0, Business: 0
--------------------------------------------------
Start Date : 24.12.2013
End Date   : 27.12.2013
Business Days (Excluding Holidays): 0
--------------------------------------------------
Calculating Business days between 7.10.2013 00:00:00 and 1.01.2014 00:00:00.
Calculating weekend days between 7.10.2013 00:00:00 and total days count: 85
Calculating remainder for total_days_count_between_dates: 85
Remainder calculated :1
Calculating quotient for total_days_count_between_dates: 85
Quotient calculated:: 12
Remainder count: 1, Quotient count: 12
Calculating remaining weekend days from start index: 1 for remainder: 1 days
Total weekend days : 24
Filtering public holidays from the generated list.
Total days: 85, Weekend days: 24, Business: 59
--------------------------------------------------
Start Date : 7.10.2013
End Date   : 1.01.2014
Business Days (Excluding Holidays): 59
--------------------------------------------------
==================================================
Task 3: Business Days with Holiday Rules
==================================================
Calculating Business days between 26.12.2022 00:00:00 and 3.01.2023 00:00:00.
Calculating weekend days between 26.12.2022 00:00:00 and total days count: 7
Calculating remainder for total_days_count_between_dates: 7
Remainder calculated :0
Calculating quotient for total_days_count_between_dates: 7
Quotient calculated:: 1
Remainder count: 0, Quotient count: 1
Total weekend days : 2
Generates based dates for certain period 
Generates based dates for certain period
Generates occurence based dates for certain period
Filtering public holidays from the generated list.
Total days: 7, Weekend days: 2, Business: 4
--------------------------------------------------
Start Date : 26.12.2022
End Date   : 3.01.2023
Business Days (Excluding Holidays): 4
--------------------------------------------------
Calculating Business days between 20.04.2023 00:00:00 and 27.04.2023 00:00:00.
Calculating weekend days between 20.04.2023 00:00:00 and total days count: 6
Calculating remainder for total_days_count_between_dates: 6
Remainder calculated :6
Calculating quotient for total_days_count_between_dates: 6
Quotient calculated:: 0
Remainder count: 6, Quotient count: 0
Calculating remaining weekend days from start index: 4 for remainder: 6 days
Remaining weekend day detected on day 2 (Index: 5)
Remaining weekend day detected on day 3 (Index: 6)
Total weekend days : 2
Generates based dates for certain period 
Generates based dates for certain period
Generates occurence based dates for certain period
Filtering public holidays from the generated list.
Total days: 6, Weekend days: 2, Business: 3
--------------------------------------------------
Start Date : 20.04.2023
End Date   : 27.04.2023
Business Days (Excluding Holidays): 3
--------------------------------------------------
Calculating Business days between 9.06.2023 00:00:00 and 15.06.2023 00:00:00.
Calculating weekend days between 9.06.2023 00:00:00 and total days count: 5
Calculating remainder for total_days_count_between_dates: 5
Remainder calculated :5
Calculating quotient for total_days_count_between_dates: 5
Quotient calculated:: 0
Remainder count: 5, Quotient count: 0
Calculating remaining weekend days from start index: 5 for remainder: 5 days
Remaining weekend day detected on day 1 (Index: 5)
Remaining weekend day detected on day 2 (Index: 6)
Total weekend days : 2
Generates based dates for certain period 
Generates based dates for certain period
Generates occurence based dates for certain period
Filtering public holidays from the generated list.
Total days: 5, Weekend days: 2, Business: 2
--------------------------------------------------
Start Date : 9.06.2023
End Date   : 15.06.2023
Business Days (Excluding Holidays): 2
--------------------------------------------------
```

**Note**: 

- If you want to edit the date range or add holiday rule or public holiday in Task 1-2-3, you can follow same instructions above.

---

## 3. How Can I Run the Unittests?

### Python Unittests
Make sure you have installed the packages, incase if you have not;

```bash
  pip install pytest
  pip install mock
  ```


```bash
  cd /design.com/python_solution
  export PYTHONPATH=$(pwd)
```

Run tests

```bash
  pytest test_validator.py
  pytest test_business_day_counter.py
  pytest test_task1.py
  pytest test_task2.py
  pytest test_task3.py
```


### .NET Unittests
I have not enough time to write unittest in .net, since having a limited of time. I hope that show you have knowledge about unittests by writing the unittests in python.

## 4. Code Documentation

### 4.1. Python

### **Class: `DayUtils`**
The main utility class for date calculations.

#### **Methods**

1. **`days_count_between_dates(start_date, end_date)`**
   - Calculates the number of full days between two dates (excluding the start date).
   - **Parameters**:
     - `start_date` (`date`): The starting date.
     - `end_date` (`date`): The ending date.
   - **Returns**:
     - `int`: The number of full days.
   - **Precondition**:
     - Dates are validated using `@validate_dates`.

2. **`remainder(total_days)`**
   - Calculates the remainder of days when dividing the total number of days by `7`.
   - **Parameters**:
     - `total_days` (`int`): Total days between two dates.
   - **Returns**:
     - `int`: Remainder days.

3. **`quotient(total_days)`**
   - Calculates the number of full weeks in the total days between two dates.
   - **Parameters**:
     - `total_days` (`int`): Total days between two dates.
   - **Returns**:
     - `int`: Number of full weeks.

4. **`total_weekend_days_count(start_date, total_days)`**
   - Determines the total number of weekend days (Saturdays and Sundays) in a date range.
   - **Parameters**:
     - `start_date` (`date`): Start date of the range.
     - `total_days` (`int`): Total days in the range.
   - **Returns**:
     - `int`: Total weekend days.

5. **`remaining_weekend_days_count(start_date_index, remainder, remaining_weekend_days)`**
   - Calculates remaining weekend days after considering full weeks.
   - **Parameters**:
     - `start_date_index` (`int`): The weekday index of the start date (0 = Monday, 6 = Sunday).
     - `remainder` (`int`): Remaining days after full weeks.
     - `remaining_weekend_days` (`int`): Running count of weekend days.
   - **Returns**:
     - `int`: Total remaining weekend days.

6. **`calculate_public_holidays(start_date, end_date, public_holiday_list)`**
   - Filters and counts public holidays within a given date range.
   - **Parameters**:
     - `start_date` (`date`): The start date.
     - `end_date` (`date`): The end date.
     - `public_holiday_list` (`list[date]`): List of all possible public holidays.
   - **Returns**:
     - `int`: Number of public holidays in the range.

7. **`filter_date(start_date, original_date, end_date)`**
   - Checks if a date falls within a specified date range.
   - **Parameters**:
     - `start_date` (`date`): Start of the range.
     - `original_date` (`date`): Date to check.
     - `end_date` (`date`): End of the range.
   - **Returns**:
     - `bool`: `True` if the date is within range, else `False`.

8. **`generates_dates_frequency_for_certain_period(start_date, period, month, day)`**
   - Generates a list of dates on a specific month and day for a given period.
   - **Parameters**:
     - `start_date` (`date`): Base date.
     - `period` (`int`): Number of years to generate dates for.
     - `month` (`int`): Desired month.
     - `day` (`int`): Desired day.
   - **Returns**:
     - `list[date]`: List of generated dates.

9. **`generates_occurrence_dates_frequency_for_certain_period(start_date, period, month, day, occurrence)`**
   - Generates dates based on the nth occurrence of a specific day in a month for a given period.
   - **Parameters**:
     - `start_date` (`date`): Base date.
     - `period` (`int`): Number of years to generate dates for.
     - `month` (`int`): Desired month.
     - `day` (`int`): Desired day.
     - `occurrence` (`int`): Nth occurrence (e.g., 1st, 2nd).
   - **Returns**:
     - `list[date]`: List of generated dates.

---

### **Class: `HolidayFactory`**

A factory class responsible for creating holiday objects based on different holiday rules and a given date range.

#### **Attributes**
- `holiday_rules` (`list`): A list of holiday rule dictionaries.
- `created_objects` (`list`): A list of created holiday objects.
- `start_date` (`datetime`): The start date for the holiday generation.
- `end_date` (`datetime`): The end date for the holiday generation.

#### **Methods**

1. **`__init__(holiday_rules, start_date, end_date)`**
   - Initializes the `HolidayFactory` object.
   - **Parameters**:
     - `holiday_rules` (`list`): Rules defining the types and properties of holidays.
     - `start_date` (`datetime`): Start date for the holiday range.
     - `end_date` (`datetime`): End date for the holiday range.

2. **`get_objects()`**
   - Creates holiday objects based on the provided holiday rules.
   - **Returns**:
     - `list`: A list of created holiday objects.
   - **Raises**:
     - `Exception`: If the holiday type is unsupported or missing.

---

### **Class: `HolidayFactoryInterface`**

An abstract base class defining the interface for holiday objects. Derived classes must implement methods to retrieve, generate, and validate holiday rules.

#### **Methods**

1. **`get_holiday()`**
   - Abstract method to retrieve holiday dates.

2. **`generate_dates()`**
   - Abstract method to generate holiday dates based on specific rules.

3. **`check_holiday()`**
   - Abstract method to validate holiday rule parameters.

---

### **Class: `PublicHoliday`**

Represents a public holiday, implementing the `HolidayFactoryInterface`.

#### **Methods**

1. **`__init__(holiday_rule, start_date, end_date)`**
   - Initializes the `PublicHoliday` object with a rule, start date, and end date.

2. **`get_holiday()`**
   - Generates and retrieves public holiday dates.
   - **Returns**:
     - `list`: List of public holiday dates.

3. **`generate_dates(*args, **kwargs)`**
   - Generates dates within the specified range.
   - **Returns**:
     - `list`: List of generated holiday dates.

4. **`check_holiday(*args, **kwargs)`**
   - Validates the holiday rule parameters.
   - **Returns**:
     - `bool`: True if parameters are valid.
   - **Raises**:
     - `Exception`: If parameters are invalid.

---

### **Class: `MoveableHoliday`**

Represents a moveable holiday, implementing the `HolidayFactoryInterface`. Adjusts holidays falling on weekends.

#### **Methods**

1. **`__init__(holiday_rule, start_date, end_date)`**
   - Initializes the `MoveableHoliday` object with a rule, start date, and end date.

2. **`move_date(date)`**
   - Adjusts a holiday if it falls on a weekend.
   - **Parameters**:
     - `date` (`datetime`): Date to be adjusted.
   - **Returns**:
     - `datetime`: Adjusted date.

3. **`generate_dates(*args, **kwargs)`**
   - Generates dates and adjusts them for weekends.
   - **Returns**:
     - `list`: List of adjusted holiday dates.

4. **`get_holiday()`**
   - Retrieves the adjusted holiday dates.
   - **Returns**:
     - `list`: List of adjusted holiday dates.

5. **`check_holiday(*args, **kwargs)`**
   - Validates the holiday rule parameters.
   - **Returns**:
     - `bool`: True if parameters are valid.
   - **Raises**:
     - `Exception`: If parameters are invalid. 

---

### **Class: `BusinessDayCounter`**

A class to calculate the number of business days, weekdays, and holidays within a date range, using utility functions and holiday rules.

#### **Methods**

---

1. **`__init__(day_utils_obj)`**  
   - Initializes the `BusinessDayCounter` with a utility object for date calculations.  
   - **Parameters**:  
     - `day_utils_obj` (`DayUtils`): An object providing utility methods for date calculations.  

---

2. **`get_total_days(start_date, end_date, total_days)`**  
   - Calculates the total number of days between two dates and adds it to the current total.  
   - **Parameters**:  
     - `start_date` (`datetime`): Start date of the range.  
     - `end_date` (`datetime`): End date of the range.  
     - `total_days` (`int`): The current total number of days.  
   - **Returns**:  
     - `int`: Updated total days, or `0` if an exception occurs.  

---

3. **`get_holidays(start_date, end_date, public_holidays, public_holiday_list=None, holiday_rules=None)`**  
   - Calculates the number of public holidays between two dates, including static and dynamically generated holidays.  
   - **Parameters**:  
     - `start_date` (`datetime`): Start date of the range.  
     - `end_date` (`datetime`): End date of the range.  
     - `public_holidays` (`int`): Initial count of public holidays.  
     - `public_holiday_list` (`list` of `datetime`, optional): List of static public holidays.  
     - `holiday_rules` (`list` of `dict`, optional): Rules for generating dynamic holidays.  
   - **Returns**:  
     - `int`: Updated public holiday count.  

---

4. **`weekdays_between_two_dates(start_date, end_date)`**  
   - Calculates the number of weekdays between two dates.  
   - **Parameters**:  
     - `start_date` (`datetime`): Start date of the range.  
     - `end_date` (`datetime`): End date of the range.  
   - **Returns**:  
     - `int`: Number of weekdays.  

---

5. **`business_days_between_two_dates(start_date, end_date, public_holiday_list=None, holiday_rules=None)`**  
   - Calculates the number of business days between two dates, excluding weekends and public holidays.  
   - **Parameters**:  
     - `start_date` (`datetime`): Start date of the range.  
     - `end_date` (`datetime`): End date of the range.  
     - `public_holiday_list` (`list` of `datetime`, optional): List of static public holidays.  
     - `holiday_rules` (`list` of `dict`, optional): Rules for generating dynamic holidays.  
   - **Returns**:  
     - `int`: Number of business days.  


---




### 4.2. Dotnet

### **Class: `BusinessDayCounter`**

A class that calculates the number of business days, weekdays, and public holidays within a given date range. It uses utility methods and handles various types of holiday rules.

#### **Methods**

---

1. **`__init__(day_utils_obj)`**  
   - Initializes the `BusinessDayCounter` with a utility object for date calculations.  
   - **Parameters**:  
     - `day_utils_obj` (`DayUtils`): An object providing utility methods for date calculations.  

---

2. **`GetTotalDays(start_date, end_date, total_days)`**  
   - Calculates the total number of days between two dates and adds it to the current total.  
   - **Parameters**:  
     - `start_date` (`datetime`): The start date of the range.  
     - `end_date` (`datetime`): The end date of the range.  
     - `total_days` (`int`): The current total number of days.  
   - **Returns**:  
     - `int`: Updated total days, or `0` if an exception occurs.

---

3. **`GetHolidays(start_date, end_date, public_holidays, public_holidays_list=None, holiday_rules=None)`**  
   - Calculates the number of public holidays between two dates, including static and dynamically generated holidays.  
   - **Parameters**:  
     - `start_date` (`datetime`): The start date of the range.  
     - `end_date` (`datetime`): The end date of the range.  
     - `public_holidays` (`int`): Initial count of public holidays.  
     - `public_holidays_list` (`list` of `datetime`, optional): List of static public holidays.  
     - `holiday_rules` (`list` of `dict`, optional): Rules for generating dynamic holidays.  
   - **Returns**:  
     - `int`: Updated public holiday count.  

---

4. **`WeekdaysBetweenTwoDates(start_date, end_date)`**  
   - Calculates the number of weekdays between two dates.  
   - **Parameters**:  
     - `start_date` (`datetime`): The start date of the range.  
     - `end_date` (`datetime`): The end date of the range.  
   - **Returns**:  
     - `int`: Number of weekdays.  

---

5. **`BusinessDaysBetweenTwoDates(start_date, end_date, public_holidays_list=None, holiday_rules=None)`**  
   - Calculates the number of business days between two dates, excluding weekends and public holidays.  
   - **Parameters**:  
     - `start_date` (`datetime`): The start date of the range.  
     - `end_date` (`datetime`): The end date of the range.  
     - `public_holidays_list` (`list` of `datetime`, optional): List of static public holidays.  
     - `holiday_rules` (`list` of `dict`, optional): Rules for generating dynamic holidays.  
   - **Returns**:  
     - `int`: Number of business days.

### **Class: `DayUtils`**


This class provides utility methods for calculating and filtering dates, including handling weekdays, weekends, holidays, and date ranges. It is useful for determining the number of business days, weekends, and public holidays between two dates.

---

### **Properties**

- **`WeekDaysRange`**  
  A `HashSet<int>` containing the indexes of weekdays (Monday to Friday), used for filtering weekdays.  
  Default value: `{0, 1, 2, 3, 4}` (Monday through Friday).

- **`WeekendDaysRange`**  
  A `HashSet<int>` containing the indexes of weekend days (Saturday and Sunday), used for filtering weekends.  
  Default value: `{5, 6}` (Saturday and Sunday).

---

### **Methods**

1. **`DaysCountBetweenDates(DateTime startDate, DateTime endDate)`**  
   - **Description**: Calculates the number of full days between two dates, excluding the start date.  
   - **Parameters**:  
     - `startDate` (`DateTime`): The start date of the range.  
     - `endDate` (`DateTime`): The end date of the range.  
   - **Returns**: `int`: The number of full days between the two dates (excluding the start date).

2. **`Remainder(int totalDays)`**  
   - **Description**: Calculates the remainder when dividing the total number of days by the number of days in a week (7).  
   - **Parameters**:  
     - `totalDays` (`int`): The total number of days.  
   - **Returns**: `int`: The remainder of the division.

3. **`Quotient(int totalDays)`**  
   - **Description**: Calculates the quotient when dividing the total number of days by the number of days in a week (7), representing the number of full weeks in the range.  
   - **Parameters**:  
     - `totalDays` (`int`): The total number of days.  
   - **Returns**: `int`: The quotient (the number of full weeks).

4. **`TotalWeekendDaysCount(DateTime startDate, int totalDays)`**  
   - **Description**: Calculates the total number of weekend days (Saturdays and Sundays) within the given date range.  
   - **Parameters**:  
     - `startDate` (`DateTime`): The start date of the range.  
     - `totalDays` (`int`): The total number of days in the range.  
   - **Returns**: `int`: The total number of weekend days.

5. **`RemainingWeekendDaysCount(int startDateIndex, int remainder, int remainingWeekendDays)`**  
   - **Description**: Calculates the remaining weekend days (Saturdays and Sundays) after considering full weeks.  
   - **Parameters**:  
     - `startDateIndex` (`int`): The weekday index of the start date (0 = Monday, 6 = Sunday).  
     - `remainder` (`int`): The number of extra days after full weeks.  
     - `remainingWeekendDays` (`int`): The count of remaining weekend days.  
   - **Returns**: `int`: The updated count of weekend days.

6. **`CalculatePublicHolidays(DateTime startDate, DateTime endDate, List<DateTime> publicHolidayList)`**  
   - **Description**: Calculates the number of public holidays within the given date range.  
   - **Parameters**:  
     - `startDate` (`DateTime`): The start date of the range.  
     - `endDate` (`DateTime`): The end date of the range.  
     - `publicHolidayList` (`List<DateTime>`): A list of public holiday dates.  
   - **Returns**: `int`: The number of public holidays within the range.

7. **`GeneratesDatesFrequencyForCertainPeriod(DateTime startDate, int period, int month, int day)`**  
   - **Description**: Generates a list of holiday dates that occur on a specific day of a month for each year in the specified period.  
   - **Parameters**:  
     - `startDate` (`DateTime`): The start date of the period.  
     - `period` (`int`): The number of years to generate holiday dates for.  
     - `month` (`int`): The month in which the holiday occurs.  
     - `day` (`int`): The day of the month when the holiday occurs.  
   - **Returns**: `List<DateTime>`: A list of holiday dates.

8. **`FilterDate(DateTime startDate, DateTime? originalDate, DateTime endDate)`**  
   - **Description**: Filters a date by checking if it falls within the specified start and end dates.  
   - **Parameters**:  
     - `startDate` (`DateTime`): The start date of the range.  
     - `originalDate` (`DateTime?`): The date to check.  
     - `endDate` (`DateTime`): The end date of the range.  
   - **Returns**: `bool`: `True` if the date is within the range, otherwise `false`.

9. **`GeneratesOccurrenceDatesFrequencyForCertainPeriod(DateTime startDate, int period, int month, int day, int occurrence)`**  
   - **Description**: Generates a list of holidays that occur on a specific weekday occurrence within a month for each year in the specified period.  
   - **Parameters**:  
     - `startDate` (`DateTime`): The start date of the period.  
     - `period` (`int`): The number of years to generate holiday dates for.  
     - `month` (`int`): The month in which the holiday occurs.  
     - `day` (`int`): The weekday of the month (e.g., Monday, Tuesday).  
     - `occurrence` (`int`): The occurrence number (e.g., 1st, 2nd, etc.).  
   - **Returns**: `List<DateTime>`: A list of holidays for the specified weekday occurrence.



---

### **Class: `HolidayFactory`**

The `HolidayFactory` class is responsible for creating different types of holiday objects based on the provided holiday rules. It handles the instantiation of moveable holidays, public holidays, and certain occurrence holidays within a given date range.

#### **Methods**

---

1. **`__init__(holidayRules, startDate, endDate)`**  
   - Initializes a new instance of the `HolidayFactory` class with the specified holiday rules, start date, and end date.  
   - **Parameters**:  
     - `holidayRules` (`List<Dictionary<string, object>>`): A list of holiday rules, each represented by a dictionary containing the necessary details.  
     - `startDate` (`DateTime`): The start date of the period to consider for holiday generation.  
     - `endDate` (`DateTime`): The end date of the period to consider for holiday generation.

---

2. **`GetObjects()`**  
   - Processes the holiday rules and creates the corresponding holiday objects based on the holiday type.  
   - **Returns**:  
     - `List<IHolidayFactoryInterface>`: A list of holiday objects, each implementing `IHolidayFactoryInterface`.  
   - **Exceptions**:  
     - Throws an exception if an unsupported holiday type is encountered or if the holiday type is missing.

---

### **Class: `PublicHoliday`**

Represents a public holiday. This class validates the holiday rule and generates the dates for a public holiday occurring every year on a fixed day and month.

#### **Methods**

---

1. **`__init__(holidayRule, startDate, endDate)`**  
   - Initializes a new instance of the `PublicHoliday` class with the specified holiday rule, start date, and end date.  
   - **Parameters**:  
     - `holidayRule` (`Dictionary<string, object>`): A dictionary containing the rule details for the holiday.  
     - `startDate` (`DateTime`): The start date of the period to consider for holiday generation.  
     - `endDate` (`DateTime`): The end date of the period to consider for holiday generation.

---

2. **`CheckHolidayRule(holidayRule)`**  
   - Validates the holiday rule to ensure the necessary keys (`month` and `day`) are present and correctly defined.  
   - **Parameters**:  
     - `holidayRule` (`Dictionary<string, object>`): The holiday rule dictionary to validate.  
   - **Returns**:  
     - `bool`: `True` if the rule is valid, otherwise throws an exception.

---

### **Class: `MoveableHoliday`**

Represents a moveable holiday. This class is used to handle holidays that change dates each year, such as Easter or Thanksgiving.

#### **Methods**

---

1. **`__init__(holidayRule, startDate, endDate)`**  
   - Initializes a new instance of the `MoveableHoliday` class with the specified holiday rule, start date, and end date.  
   - **Parameters**:  
     - `holidayRule` (`Dictionary<string, object>`): A dictionary containing the rule details for the holiday.  
     - `startDate` (`DateTime`): The start date of the period to consider for holiday generation.  
     - `endDate` (`DateTime`): The end date of the period to consider for holiday generation.

---

2. **`GenerateHolidayDates()`**  
   - Generates the dates for the moveable holiday based on the provided rules and date range.  
   - **Returns**:  
     - `List<DateTime>`: A list of `DateTime` objects representing the moveable holiday dates within the specified range.

---

### **Class: `CertainOccurrenceHoliday`**

Represents a holiday that occurs on a specific weekday (e.g., the first Monday of a month). This class handles the generation of dates for holidays with specific weekday occurrences.

#### **Methods**

---

1. **`__init__(holidayRule, startDate, endDate)`**  
   - Initializes a new instance of the `CertainOccurrenceHoliday` class with the specified holiday rule, start date, and end date.  
   - **Parameters**:  
     - `holidayRule` (`Dictionary<string, object>`): A dictionary containing the rule details for the holiday.  
     - `startDate` (`DateTime`): The start date of the period to consider for holiday generation.  
     - `endDate` (`DateTime`): The end date of the period to consider for holiday generation.

---

2. **`GenerateHolidayDates()`**  
   - Generates the dates for the certain occurrence holiday based on the provided rules and date range.  
   - **Returns**:  
     - `List<DateTime>`: A list of `DateTime` objects representing the certain occurrence holiday dates within the specified range.

---

### **Interface: `IHolidayFactoryInterface`**

This interface is implemented by all holiday classes to ensure a uniform structure for holiday generation. It includes the method to generate holiday dates.

#### **Methods**

---

1. **`GenerateHolidayDates()`**  
   - Generates the dates for the specific type of holiday.  
   - **Returns**:  
     - `List<DateTime>`: A list of `DateTime` objects representing the holiday dates within the specified range.

---


## 5. TODO's

- **Add More Unit Tests**: Cover edge cases and ensure all holiday scenarios are thoroughly tested.
- **Improve Code Comments and Logging**: Add more in-depth comments/logging for better readability, especially for complex methods.
- **Cross-Platform Testing**: Ensure the Python and .NET code work seamlessly across different environments and versions. We can dockerize the projects.
- **Connect and Customize the logging to alert based services**: Integrate to logging class to alert based services such as Sentry or Prometheus to monitor

---
