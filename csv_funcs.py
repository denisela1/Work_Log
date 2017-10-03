import csv
from datetime import datetime
import menu
import re


def read_dates():
    with open("logs.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        i = 0
        for row in reader:
            print(i, row[0], row[1])
            i += 1
        index = int(input("Enter the number of the task number to list the details:\n"))
        with open("logs.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            output = list(reader)
            print((", ".join(output[index])))
    select = (str(input("To quit, press Q. "
                            "To go back to the main menu, press any letter.\n"))).upper()
    if select == "Q":
        print("You quit.\n")
    else:
        menu.main_screen()


def read_time():
    while True:
        try:
            index = str(input("Enter the total amount of minutes spent to list associated tasks:\n"))
            with open("logs.csv", 'r') as csvfile:
                reader = csv.reader(csvfile)
                i = 0
                results = []
                for row in reader:
                    results.append(row)
                    i += 1
                    if index in row:
                        print(i,row)
                selection = int(input("Select the number of the task (on the left side) you'd like to list the details of.\n"))
                print(results[selection-1])
                select = (str(input("To quit, press Q. "
                            "To go back to the main menu, press any letter.\n"))).upper()
                if select == "Q":
                    print("You quit.\n")
                else:
                    menu.main_screen()
        except ValueError:
            print('Sorry, please enter a valid value')
        else:
            break


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
                    select = (str(input("Sorry, no task and/or note found."
                                        "To quit, press Q. "
                                        "To go back to the main menu, press any letter.\n"))).upper()
                    if select == "Q":
                        print("You quit.\n")
                    else:
                        menu.main_screen()
        except ValueError:
            print('Sorry, please enter a valid value')
        else:
            break


def read_pattern(pattern):
    while True:
        try:
            with open("logs.csv", 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    for value in row:
                        match = re.search(pattern, value)
            print(match)
        except ValueError:
            print('Sorry, please enter a valid value')
        else:
            break


def writef():
    with open("logs.csv", 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        while True:
            try:
                date_input = (datetime.strptime(input('Enter a date (MM/DD/YYYY).\n'), '%m/%d/%Y')).date()
                task_input = input('Enter the name of the task.\n')
                time_input = int(input('Enter minutes spent:\n'))
                notes_input = str(input('Enter any additional notes:\n'))
                select = (str(input("Entry recorded. To quit, press Q. "
                                    "To go back to the main menu, press any letter.\n"))).upper()
                if select == "Q":
                    print("You quit.\n")
                    break
                else:
                    menu.main_screen()
            except ValueError:
                print('Sorry, please enter a valid value')
            else:
                break
        writer.writerow([date_input, task_input, time_input, notes_input])
