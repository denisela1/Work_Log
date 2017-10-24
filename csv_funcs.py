import csv
from datetime import datetime
import re
import os


def clear():
    """Function to clear screen as the program runs."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def read_file():
    """
    Function to read the csv file and return data as a dictionary, dates being the keys and tasks, time, notes are
    the values.
    {'2017-10-14': [ {'name': 'Task', 'time': '10', 'notes': ''} ]}
    """
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


def show_options(data):
    """
    Function to display date options after the user input.
    This function is formatted to be used after the search logic in each search function.
    """
    indexed = {}
    for i, v in enumerate(data):
        print(i + 1, v)
        indexed.update({i + 1: v})
    return indexed


def show_results(dictionary, selection):
    """
    Function to display results based on the selected date.
    If a date (the key of the dictionary) has more than one entry, this function will make sure to provide these options
    Otherwise, only one result will be shown.
    """
    for key, value in dictionary.items():
        if selection == key:
            for i in value:
                print(key)
                for keys, values in i.items():
                    print(keys, values)
                print('\t')


def show_details(filtered_dictionary):
    """
    After the search results are shown and final selection is made, this function organizes the data to be included in
    the final results/details. It's formatted to be used by each search function.
    """
    display_dictionary = show_options(filtered_dictionary.keys())
    index = int(input("Please select a date to list the details by entering its number on the left side:\n"))
    selection = display_dictionary[index]
    show_results(filtered_dictionary, selection)


def read_dates():
    """
    Function to read dates in the csv file and return entries based on the date selected by the user.
    Data is stored as a dictionary, dates being the keys.
    """
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


def read_time():
    """
    Function to run the search logic to find entries by time.
    The search logic filters the data and stores it in a variable called 'filtered_dictionary'.
    Filtered_dictionary is passed to the function 'show_details' to list the details.
    """
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


def read_string():
    """
    Function to run the search logic to find entries by exact match.
    The search logic filters the data and stores it in a variable called 'filtered_dictionary'.
    Filtered_dictionary is passed to the function 'show_details' to list the details.
    """
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


def read_pattern():
    """
    Function to run the search logic to find entries by pattern.
    The search logic filters the data and stores it in a variable called 'filtered_dictionary'.
    Filtered_dictionary is passed to the function 'show_details' to list the details.
    """
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


def write_file():
    """Function to enter a new log to the csv file and make sure the user input is in the required format."""
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
