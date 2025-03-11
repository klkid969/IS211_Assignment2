import urllib.request

def downloadData(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8') #Decodes the byte data into string data.
    return data

import urllib.request
import datetime
import csv
import logging

def processData(file_content):
    person_data = {}
    logger = logging.getLogger('assignment2')
    lines = file_content.splitlines()
    reader = csv.reader(lines)
    next(reader) #Skip the header line.
    for line_num, row in enumerate(reader, start=1):
        try:
            id_num, name, birthday_str = row
            day, month, year = map(int, birthday_str.split('/'))
            birthday = datetime.date(year, month, day)
            person_data[id_num] = (name, birthday)
        except (ValueError, IndexError) as e:
            logger.error(f"Error processing line #{line_num} for ID #{row[0] if len(row) > 0 else 'Unknown'}")
    return person_data

def displayPerson(id_num, person_data):
    if id_num in person_data:
        name, birthday = person_data[id_num]
        print(f"Person #{id_num} is {name} with a birthday of {birthday.strftime('%YYYY-%mm-%dd')}")
    else:
        print("No user found with that id")

import argparse
import urllib.request
import datetime
import csv
import logging

# ... (Previous functions: downloadData, processData, displayPerson)

def setup_logger():
    logger = logging.getLogger('assignment2')
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler('errors.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def main():
    parser = argparse.ArgumentParser(description="Process person data from a URL.")
    parser.add_argument('--url', required=True, help="URL of the CSV file.")
    args = parser.parse_args()

    setup_logger()

    try:
        csv_data = downloadData(args.url)
    except urllib.error.URLError as e:
        print(f"Error downloading data: {e}")
        return

    person_data = processData(csv_data)

    while True:
        try:
            id_num = int(input("Enter an ID to lookup (or 0 or negative to exit): "))
            if id_num <= 0:
                break
            displayPerson(str(id_num), person_data)
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()