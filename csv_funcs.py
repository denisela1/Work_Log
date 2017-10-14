import csv
from datetime import datetime
import menu
import re
import itertools


# Function to read dates in the csv file and return entries based on the date selected by the user
def read_file(index=None):
    with open("logs.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        results = list(reader)
        dates_only = []
        for item in results:
            if item[0] not in dates_only:
                dates_only.append(item[0])

        if index is None:
            output = output.join(dates_only)
        else:
            output = output.join(dates_only[index])
        print(output)



def read_dates():
    read_file()
    return
    titles = ['Date', 'Task', 'Minutes Spent', 'Notes']
    with open("logs.csv", 'r') as csvfile1:
        reader = csv.reader(csvfile1)
        results = []
        final = []
        entry = ''
        i = 0
        for row in reader:
            if row[0] not in results:
                results.append((row[0]))
                print(i, row[0])
                i += 1
        index = int(input("Please select a date to list the details by entering its number on the left side:\n"))
        if index > i:
            print("Not a valid selection. Please try again.")
            read_dates()
        else:
            entry = results[index]
        with open("logs.csv", 'r') as csvfile2:
            reader = csv.reader(csvfile2)
            for row in reader:
                if entry in row[0]:
                    final.append(row)
            for i in final:
                dictionary = dict(zip(titles, i))
                print(str(dictionary).replace("{", "").replace("}", ""))
        print("\n")
    # menu.main_screen()


# Function to read time associated with tasks in the csv file and return the entries based on
# the time entered by the user
def read_time() -> object:
    titles = ['Date', 'Task', 'Minutes Spent', 'Notes']
    while True:
        try:
            index = str(input("Enter the total amount of minutes spent to list associated tasks:\n"))
            with open("logs.csv", 'r') as csvfile:
                reader = csv.reader(csvfile)
                results = []
                c = 1
                for row in reader:
                    if row[2] == index:
                        results.append(row)
                for i in results:
                    dictionary = dict(zip(titles, i))
                    print(c, str(dictionary).replace("{", "").replace("}", ""))
                    c += 1
                if len(results) != 0:
                    selection = int(input("Select the number of the task (on the left side) you'd like to list "
                                          "the details of.\n"))
                    selected = results[selection-1]
                    dictionary = dict(zip(titles, selected))
                    print(str(dictionary).replace("{", "").replace("}", ""))
                else:
                    print("Sorry, no entry found.")
                    # menu.main_screen()
        except ValueError:
            print('Sorry, your entry is not valid.\n')
        else:
            break


# Function to read task names and notes for each entry in the csv file and return the entries based on exact match
# of the user input
def read_string():
    while True:
        try:
            keyword = (str(input("Enter a keyword to search for a specific task or note.\n"))).lower()
            with open("logs.csv", 'r') as csvfile:
                reader = csv.reader(csvfile)
                i = 0
                for row in reader:
                    if keyword in row[1].lower():
                        if keyword in row[3].lower():
                            print("Entries found:")
                            print(row)
                            i += 1
                        else:
                            print("Entries found:")
                            print(row)
                            i += 1
                if i == 0:
                    print("Sorry, no task and/or note found.\n")
        except ValueError:
            print('Sorry, please enter a valid value')
        else:
            break
    # menu.main_screen()


# Function to read pattern as a regular expression entered by the user and return the entries that match
def read_pattern():
    titles = ['Date', 'Task', 'Minutes Spent', 'Notes']
    while True:
        try:
            with open("logs.csv", 'r') as csvfile:
                reader = csv.reader(csvfile)
                pat = str(input("Please enter a pattern (e.g. \w).\n"))
                results = []
                for row in reader:
                    for value in row[1] or row[3]:
                        match = re.findall(pat, value)
                        if match:
                            results.append(row)
            final = list(results for results, _ in itertools.groupby(results))
            for i in final:
                dictionary = dict(zip(titles, i))
                print(str(dictionary).replace("{", "").replace("}", ""))
        except ValueError:
            print('Sorry, please enter a valid value')
        else:
            break


# Function to enter a new log to the csv file
def write_file():
    with open("logs.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        date_input = None
        task_input = ''
        time_input = None
        while True:
            try:
                if date_input is None:
                    date_input = (datetime.strptime(input('Enter a date (MM/DD/YYYY).\n'), '%m/%d/%Y')).date()
                if not task_input:
                    task_input = input('Enter the name of the task.\n')
                if time_input is None:
                    time_input = int(input('Enter minutes spent:\n'))
                notes_input = str(input('Enter any additional notes:\n'))
                select = (str(input("Entry recorded. To quit, press Q. "
                                    "To go back to the main menu, press any letter.\n"))).upper()
                if select == "Q":
                    print("You quit.\n")
                    break
                else:
                    # menu.main_screen()
                    pass
            except ValueError:
                print('Sorry, please enter a valid value')
            else:
                print('this happened')
                break
        writer.writerow([date_input, task_input, time_input, notes_input])
