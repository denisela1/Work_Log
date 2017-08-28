import os
from entry import Entry
import csv_funcs

# First screen to make a selection: new entry, search entry or quit
def main_screen():
    selection = (input("To make an entry, press E."
                       "To look up a previous entry, press S."
                       "To quit, press Q.\n")).upper()
    if selection == 'E':
        selected = Entry()
        selected.add_entry()
    if selection == 'S':
        selected = (input("To search by date, press D.\n"
                         "To search by time spent, press T.\n"
                         'To search by exact match, press E.\n'
                         "To search by pattern, press P.\n")).upper()
        if selected == 'D':
           search_date()

        if selected == 'T':
            time_spent = input('Enter the number of minutes of a task took:\n')
            search_time_spent(time_spent)
        if selected == 'E':
            exact_entry = input('Enter a date to look up for a specific entry.\n')
            search_exact_entry(exact_entry)
        if selected == 'P':
            pattern = input('Enter a pattern to look up for a specific entry based on its task and notes.\n')
            search_pattern(pattern)
    if selection == 'Q':
        print("You quit")
        clear()


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
     main_screen()
