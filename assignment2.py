import csv

def read_csv(file_name):
    """Reads the CSV file and returns a list of dictionaries."""
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def display_birthdays(data):
    """Displays the names and birthdays."""
    for entry in data:
        print(f"Name: {entry['name']}, Birthday: {entry['birthday']}")

def main():
    file_name = 'birthdays100.csv'
    data = read_csv(file_name)
    display_birthdays(data)

if __name__ == "__main__":
    main()
