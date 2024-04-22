# 1. Name:
#      Isaiah Page
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program will take two dates and find the number of days in between them.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part of this assignment was making sure that all of the inputs
#      were handled correctly, meaning that there was proper validation and error catching.
#      I had to do extra research on how to validate certain data types in cojunction with other criteria.
# 5. How long did it take for you to complete the assignment?
#      It took me about two hours with another hour of research, so three total.

def main():
    date_1 = get_valid_date("Start") # Start date

    date_2 = get_valid_date("End") # End date

    days_1 = convert_to_days(date_1) # Convert date to days
    days_2 = convert_to_days(date_2)

    difference = abs(days_1 - days_2)  # difference in days between the dates

    return print(difference)

def get_valid_date(prompt):
    """
    Prompt the user to input valid year, month, and day.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        tuple: A tuple containing the valid year, month, and day as integers.
    """
    while True:
        try:
            year = int(input(prompt + " (Year): "))
            month = int(input(prompt + " (Month): "))
            day = int(input(prompt + " (Day): "))
            
            if year < 1753:
                raise ValueError("Year must be after 1753.")
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")
            if day < 1 or day > 31:
                raise ValueError("Day must be between 1 and 31.")

            # Check if the day is valid for the given month and year
            max_days = (31, 29 if is_leap_year(year) and month == 2 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[month - 1]
            if day > max_days:
                raise ValueError("Day exceeds maximum days for the given month and year.")

            return year, month, day

        except ValueError as ve:
            print("Invalid input:", ve)
            print("Please enter valid numeric values.")

def convert_to_days(date):
    """
    Turns a complete date of year month and day into just days.

    Args:
        date (tuple): A tuple containing year, month, and day.
    Returns:
        total_days (int): the date value converted into days.
    """
    year, month, day = date
    total_days = 0  # initialize total days variable

    for y in range(1, year - 1):  # finding the total days for each year and adding them
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365
    
    for m in range(1, month - 1):  # finding the total days for each month until the current one
        days_in_month = get_days_in_month(m, year)
        total_days += days_in_month

    total_days += day  # adding the days into the total days

    return total_days

def get_days_in_month(month, year):  
    """
    Gets the days in the month.

     Args:
        month (int): the month to check
        year (int): year of that month
    Returns:
        days_in_month (int): the days in that month
    """
    # list that has the days each month has
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
     
    if month == 2 and is_leap_year(year): # Checking if Feb has 28 or 29 for that year
        return 29     
    else: 
        return days_in_month[month - 1] 
    
def is_leap_year(year):
    """
    Check if a given year is a leap year.

    Args:
        year (int): The year to be checked.
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:  # If the year is divisible by 4
        if year % 100 == 0:  # If the year is divisible by 100
            if year % 400 == 0:  # If the year is divisible by 400
                return True  # Leap year
            else:
                return False  # Not a leap year
        else:
            return True  # Leap year
    else:
        return False  # Not a leap year


if __name__ == "__main__":
    main()
