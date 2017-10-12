import os
import csv_funcs


# First screen for the user to make a selection: new entry, search entry or quit.
def main_screen():
    selection = (input("For a new entry, press E.\n"
                       "To find a previous entry, press S.\n"
                       "To quit, press Q.\n")).upper()
    if selection == 'E':
        csv_funcs.write_file()
    if selection == 'S':
        search_menu()
    if selection == 'Q':
        print("You quit")
        clear()
    else:
        print('Please try again.\n')


# If the user selects "search" option, the following screen will appear, giving the user 4 options to run a search:
# By date, by time spent, by exact match and by pattern/regular expression.
def search_menu():
    selected = (input("To search by date, press D.\n"
                      "To search by time spent, press T.\n"
                      "To search by exact match, press E.\n"
                      "To search by pattern, press P.\n"
                      "To quit, press Q.\n")).upper()
    if selected == 'D':
        csv_funcs.read_dates()
    if selected == 'T':
        csv_funcs.read_time()
    if selected == 'E':
        csv_funcs.read_string()
    if selected == 'P':
        csv_funcs.read_pattern()
    if selected == 'Q':
        quit_f()
    else:
        print("Not a valid selection.\n")


# Function to quit
def quit_f():
    print("You quit\n")


# Function to clear screen as the program runs
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# To make sure program doesn't run when modules are only imported
if __name__ == '__main__':
    main_screen()

