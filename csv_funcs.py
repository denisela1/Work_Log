import csv
from datetime import datetime
import menu
import re
import itertools
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
            date, task, mins, notes = i[0],i[1],i[2],i[3]
            details = {'name': task, 'time': mins, 'notes': notes}
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


# Function to read dates in the csv file and return entries based on the date selected by the user.
# First, storing the values of the read_file() function
def read_dates():
    dictionary = read_file()
    while True:
        display_dictionary = show_options(dictionary.keys())
        index = int(input("Please select a date to list the details by entering its number on the left side:\n"))
        selection = display_dictionary[index]
        show_results(dictionary, selection)
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
                    if v['time'] == search:
                        match.append(key)
            filtered_dictionary = dict((k, dictionary[k]) for k in match if k in dictionary)
            for v in filtered_dictionary.values():
                for i in v:
                    if i['time'] != search:
                        v.remove(i)
            display_dictionary = show_options(filtered_dictionary.keys())
            index = int(input("Please select a date to list the details by entering its number on the left side:\n"))
            selection = display_dictionary[index]
            show_results(filtered_dictionary, selection)
        except ValueError:
            print('Sorry, your entry is not valid.\n')
        else:
            break


# Previous code
def read_time1():
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
        dictionary = read_file()
        match = []
        try:
            search = str(input("Enter a keyword to search for a specific task or note:\n")).lower()
            for key, value in dictionary.items():
                for v in value:
                    if search in (v['name']).lower():
                        match.append(key)
            filtered_dictionary = dict((k, dictionary[k]) for k in match if k in dictionary)
            for v in filtered_dictionary.values():
                for i in v:
                    if (i['name']).lower() != search:
                        v.remove(i)
            display_dictionary = show_options(filtered_dictionary.keys())
            index = int(input("Please select a date to list the details by entering its number on the left side:\n"))
            selection = display_dictionary[index]
            show_results(filtered_dictionary, selection)
        except ValueError:
            print('Sorry, your entry is not valid.\n')
        else:
            break


# Previous code
def read_string1():
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
    while True:
        dictionary = read_file()
        print(dictionary)
        match = []
        try:
            search = str(input("Please enter a pattern (e.g. \w).\n"))
            for key, value in dictionary.items():
                for v in value:
                    match = re.findall(search, v['name'])
                    if match:
                        match.append(key)
            filtered_dictionary = dict((k, dictionary[k]) for k in match if k in dictionary)
            print(filtered_dictionary)
            for v in filtered_dictionary.values():
                for i in v:
                    match = re.findall(search, i['name'])
                    if not match:
                        v.remove(i)
            display_dictionary = show_options(filtered_dictionary.keys())
            index = int(input("Please select a date to list the details by entering its number on the left side:\n"))
            selection = display_dictionary[index]
            show_results(filtered_dictionary, selection)
        except ValueError:
            print('Sorry, your entry is not valid.\n')
        else:
            break


# Previous code
def read_pattern1():
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
