import csv
from datetime import datetime

def readf():
    data = []
    with open("logs.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            date = (datetime.strptime(row[0], '%m/%d/%Y')).date()
            task_name = row[1]
            time_spent = (datetime.strptime(row[2], '%H:%M')).time()
            notes = row[3]
    data.append([date,task_name,time_spent,notes])
    print(data)

def writef():
    with open("logs.csv", 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        date_input = input('Enter a date (MM/DD/YYY).\n')
        task_input = input('Enter the name of the task.\n')
        time_input = input('Enter amount of time spent (HH:MM):\n')
        notes_input = input('Enter any additional notes:\n')
        writer.writerow([date_input, task_input, time_input, notes_input])

