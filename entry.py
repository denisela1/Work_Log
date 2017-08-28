import csv_funcs

#Class Entry is for creating new, updating and deleting entries.
class Entry():
    #Init method to create an empty list for the result
    def __init__(self):
        pass

    #Class method to add an entry by providing a task name, a number of minutes spent working on it and any additional
    # notes.
    def add_entry(self):
        csv_funcs.writef()

    # Class method to find a previous entry by date.
    def search_date(self):
        print("Choose one to see entries from:\n")
        #date_list import from the csv file, specific rows to list the dates.
        #provide a menu of selection e.g. 1. 08/08/2017, etc.

    #Class method to find a previous entry by time spent.
    def search_time_spent(self, time_spent):
        print(time_spent)
        #look up from the csv file to find the amount spent and list the entries
        #let the user choose from the entries, containing that string in the task name or notes
        #display the result
        #go back to the main menu or quit
    # Class method to find a previous entry by exact search.

    def search_exact_entry(self, exact_entry):
        print(exact_entry)
        #read the csv file to find the exact date and return the entries

    # Class method to find a previous entry by pattern.
    def search_pattern(self, pattern):
        print(pattern)
        #regular expression stuff enter a regular expression and then be presented with entries matching that
        # pattern in their task name or notes.

