import csv
from datetime import datetime
import re
import os


# Function to clear screen as the program runs
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Function to read the csv file and return data as a dictionary, dates being the keys and tasks, time, notes
# are the values
def read_file():
    # {'2017-10-14': [ {'name': 'Task', 'time': '10', 'notes': ''} ]}
    with open("logs.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        result = list(reader)
        dictionary = {}
        for i in result[1:]:
            date, task, mins, notes = i[0], i[1], i[2], i[3]
            details = {'Name': task, 'Time': mins, 'Notes': notes}
            if date in dictionary.keys():
                dictionary[date].append(details)
            else:
                dictionary.update({date: [details]})
        return dictionary


# Function to display options using the dictionary format, only unique dates are shown
def show_options(data):
    indexed = {}
    for i, v in enumerate(data):
        print(i + 1, v)
        indexed.update({i + 1: v})
    return indexed


# Function to display results based on search options
def show_results(dictionary, selection):
    for key, value in dictionary.items():
        if selection == key:
            for i in value:
                print(key)
                for keys, values in i.items():
                    print(keys, values)
                print('\t')


# Function to display the details based on user selection
def show_details(filtered_dictionary):
    display_dictionary = show_options(filtered_dictionary.keys())
    index = int(input("Please select a date to list the details by entering its number on the left side:\n"))
    selection = display_dictionary[index]
    show_results(filtered_dictionary, selection)


# Function to read dates in the csv file and return entries based on the date selected by the user.
# First, storing the values of the read_file() function
def read_dates():
    dictionary = read_file()
    while True:
        show_details(dictionary)
        prompt = input('\nPress Q to quit or R to return to selection screen.\n')
        if prompt == 'R':
            continue
        elif prompt == 'Q':
            break
        else:
            print("Not a valid option. Please try again.")


# Function to read time associated with tasks in the csv file and return the entries based on
# the time entered by the user
def read_time():
    while True:
        dictionary = read_file()
        match = []
        try:
            search = str(input("Enter the total amount of minutes spent to list associated tasks:\n"))
            for key, value in dictionary.items():
                for v in value:
                    if v['Time'] == search:
                        match.append(key)
            filtered_dictionary = dict((k, dictionary[k]) for k in match if k in dictionary)
            for v in filtered_dictionary.values():
                for i in v:
                    if i['Time'] != search:
                        v.remove(i)
            show_details(filtered_dictionary)
        except ValueError:
            print('Sorry, your entry is not valid.\n')
        else:
            break


# Function to read task names and notes for each entry in the csv file and return the entries based on exact match
# of the user input
def read_string():
    while True:
        dictionary = read_file()
        match = []
        try:
            search = str(input("Enter a keyword to search for a specific task or note:\n")).lower()
            for key, value in dictionary.items():
                for v in value:
                    if search in (v['Name']).lower():
                        match.append(key)
            filtered_dictionary = dict((k, dictionary[k]) for k in match if k in dictionary)
            for v in filtered_dictionary.values():
                for i in v:
                    if (i['Name']).lower() != search:
                        v.remove(i)
            show_details(filtered_dictionary)
        except ValueError:
            print('Sorry, your entry is not valid.\n')
        else:
            break


# Function to read pattern as a regular expression entered by the user and return the entries that match
def read_pattern():
    while True:
        dictionary = read_file()
        filtered = []
        try:
            search = str(input("Please enter a pattern (e.g. \w).\n"))
            for key, value in dictionary.items():
                for v in value:
                    match_name = re.findall(search, v['Name'])
                    match_notes = re.findall(search, v['Notes'])
                    if match_name or match_notes:
                        filtered.append(key)
            filtered_dictionary = dict((k, dictionary[k]) for k in filtered if k in dictionary)
            for v in filtered_dictionary.values():
                for i in v:
                    match_name = re.findall(search, i['Name'])
                    match_notes = re.findall(search, i['Notes'])
                    if not match_name or not match_notes:
                        v.remove(i)
            show_details(filtered_dictionary)
        except ValueError:
            print('Sorry, your entry is not valid.\n')
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
                    pass
            except ValueError:
                print('Sorry, please enter a valid value')
            else:
                print('\t')
                break
        writer.writerow([date_input, task_input, time_input, notes_input])
