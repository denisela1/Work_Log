import os
import csv_funcs

#Class Entry is for creating new, updating and deleting entries.
class Entry():
    #Init method to create an empty list for the result
    def __init__(self) -> object:
        pass

    #Class method to add an entry by providing a task name, a number of minutes spent working on it and any additional
    # notes.
    def add_entry(self):
        csv_funcs.writef()

    # Class method to find a previous entry by date.
    def search_date(self):
        print("Choose one to see entries from:\n")
        csv_funcs.read_dates()

    #Class method to find a previous entry by time spent.
    def search_time(self):
        csv_funcs.read_time()

    # Class method to find a previous entry by exact search.
    def search_string(self):
        csv_funcs.read_string()

    # Class method to find a previous entry by pattern.
    def search_pattern(self, pattern):
        csv_funcs.read_pattern(pattern)


# First screen to make a selection: new entry, search entry or quit.
# Based on the selection, csv file specific functions will be run.
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
            selected = Entry()
            selected.search_date()
        if selected == 'T':
            selected = Entry()
            selected.search_time()
        if selected == 'E':
            selected = Entry()
            selected.search_string()
        if selected == 'P':
            selected = Entry()
            pattern = str(input("Enter a pattern\n"))
            selected.search_pattern(pattern)
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
