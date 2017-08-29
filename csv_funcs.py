import csv
from datetime import datetime
import menu


def read_dates():
    with open("logs.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            print(i, row[0], row[1])
            i += 1
        index = int(input("Enter the number of the date/task as seen on the screen:\n"))
        data = list(reader)
        print(data[index])

def read_time():
    with open("logs.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            print(i, row[2])
            i += 1
        index = int(input("Enter the number of the task with requested minute spent:\n"))
        data = list(reader)
        print(data[index])

def read_string():
    with open("logs.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        keyword = str(input("Enter a keyword to search for a specific task or note.\n"))
        for row in reader:
            if keyword.lower() in (row[1]).lower():
                print("Task including the keyword:\n",row[0], row[1], row[2], row[3])
        for row in reader:
            if keyword.lower() in (row[3]).lower():
                print("Notes including the keyword:\n",row[0], row[1], row[2], row[3])

#def read_pattern():
    #with open("logs.csv", 'r') as csvfile:
        #reader = csv.reader(csvfile)
        #for row in reader:

def writef():
    with open("logs.csv", 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        while True:
            try:
                date_input = (datetime.strptime(input('Enter a date (MM/DD/YYYY).\n'), '%m/%d/%Y')).date()
                task_input = input('Enter the name of the task.\n')
                time_input = int(input('Enter minutes spent:\n'))
                notes_input = str(input('Enter any additional notes:\n'))
                select = (str(input("Entry recorded. To quit, press Q. To go back to the main menu, press any letter.\n"))).upper()
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
