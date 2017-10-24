import csv_funcs


def main_screen():
    """First screen for the user to make a selection: new entry, search entry or quit."""
    while True:
        csv_funcs.clear()
        selection = (input("For a new entry, press E.\n"
                           "To find a previous entry, press S.\n"
                           "To quit, press Q.\n")).upper()
        if selection == 'E':
            csv_funcs.write_file()
        elif selection == 'S':
            search_menu()
        elif selection == 'Q':
            print("You quit")
            break
        else:
            print('Please try again.\n')


def search_menu():
    """
    If the user selects "search" option, the following screen will appear, giving the user 4 options to run a search:
    By date, by time spent, by exact match and by pattern/regular expression.
    """
    selected = (input("To search by date, press D.\n"
                      "To search by time spent, press T.\n"
                      "To search by exact match, press E.\n"
                      "To search by pattern, press P.\n"
                      "To go back to the main menu, press Q.\n")).upper()
    if selected == 'D':
        csv_funcs.read_dates()
    elif selected == 'T':
        csv_funcs.read_time()
    elif selected == 'E':
        csv_funcs.read_string()
    elif selected == 'P':
        csv_funcs.read_pattern()
    elif selected == 'Q':
        print("You quit\n")
    else:
        print("Not a valid selection.\n")


if __name__ == '__main__':
    main_screen()

