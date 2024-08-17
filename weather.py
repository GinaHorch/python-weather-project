import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    try:
        float(temp)
        return f"{temp}{DEGREE_SYMBOL}"
    except ValueError:
        raise ValueError("The provided temperature must be a valid number.")
    

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    try:
        date_object = datetime.fromisoformat(iso_string)
        return date_object.strftime("%A %d %B %Y") 
    except ValueError:
        raise ValueError("The provided date must be in ISO format (YYYY-MM-DD).")


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    try:
        temp_in_fahrenheit = float(temp_in_fahrenheit)
    except ValueError:
        raise ValueError("The provided value must be a number.")
   
    temp_in_celcius = (temp_in_fahrenheit - 32) * 5.0 / 9.0
    return round(temp_in_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    converted_data = [] #test with string input kept failing, so convert data first before calculating mean


    for item in weather_data:
        if isinstance(item, str):
            try:
                item = float(item) if '.' in item else int(item)
            except ValueError:

                raise ValueError(f"Cannot convert '{item} to a number.")
        elif not isinstance(item, (int, float)):
            raise ValueError(f"Invalid type: '{item}' is not a number")
        
        converted_data.append(item)

    mean_value = sum(converted_data) / len(converted_data) #don't forget using the converted data, otherwise you keep failing the test

    return mean_value


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    
    data_list = []

    try:
        with open(csv_file, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader) #skip the header row, otherwise you get an AssertionError
            for row in csv_reader:
                if row: #make sure the row is not empty
                    row[1] = int(row[1]) #kept getting an error that the lists differ from the expected output
                    row[2] = int(row[2])
                    data_list.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {csv_file} does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file: {e}")
    
    return data_list

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()   #check if the list is empty, make sure you return an empty tuple if the list is empty
    
    for index, value in enumerate(weather_data):    #convert all string numbers to floats
        if isinstance(value, str):
            try:
                weather_data[index] = float(value)
            except ValueError:
                raise ValueError(f"Cannot convert '{value}' to a number.")
        elif not isinstance(value, (int, float)):
            raise ValueError(f"Invalid type: {value} is not a number")

    min_value = weather_data[0]     #tests fail if you don't initialise the minimum value and index
    min_index = 0

    for index, value in enumerate(weather_data):    #enumerate gives you value and index
        if value <= min_value:
            min_value = value
            min_index = index

    return min_value, min_index

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()   #check if the list is empty, make sure you return an empty tuple if the list is empty
    
    for index, value in enumerate(weather_data):    #convert all string numbers to floats
        if isinstance(value, str):
            try:
                weather_data[index] = float(value)
            except ValueError:
                raise ValueError(f"Cannot convert '{value}' to a number.")
        elif not isinstance(value, (int, float)):
            raise ValueError(f"Invalid type: {value} is not a number")

    max_value = weather_data[-1]     #tests fail if you don't initialise the minimum value and index
    max_index = -1

    for index, value in enumerate(weather_data):    #enumerate gives you value and index
        if value >= max_value:
            max_value = value
            max_index = index

    return max_value, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
