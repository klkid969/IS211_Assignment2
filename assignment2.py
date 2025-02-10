import logging

# Set up logging to a file named 'errors.log'
logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(message)s')
logger = logging.getLogger('assignment2')

import csv
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(message)s')
logger = logging.getLogger('assignment2')

def read_csv(file_name):
    """Reads the CSV file and returns a list of dictionaries."""
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def calculate_age(birthday_str):
    """Calculates age from the birthday string (dd/mm/yyyy format)."""
    try:
        birthdate = datetime.strptime(birthday_str, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    except ValueError:
        return None  # Return None if the date is invalid

def process_and_display_birthdays(data):
    """Processes birthdays, calculates age, and logs errors for malformed dates."""
    for entry in data:
        name = entry['name']
        birthday = entry['birthday']
        
        # Try to calculate age
        age = calculate_age(birthday)
        if age is None:
            # Log the error for malformed date
            logger.error(f"Error processing line for ID #{entry['id']}: Invalid date {birthday}")
            print(f"Name: {name}, Birthday: {birthday} - ERROR: Invalid date")
        else:
            print(f"Name: {name}, Birthday: {birthday}, Age: {age}")

def main():
    file_name = 'birthdays100.csv'  # Update the path if needed
    data = read_csv(file_name)
    process_and_display_birthdays(data)

if __name__ == "__main__":
    main()
