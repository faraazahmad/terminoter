# import the source file containing the db handling class
import db

# imoprt sys library to access command line arguments
import sys

# search for argument in inputs and decide the action
# to perform based on the argument, with the succeeding
# list item as argument
def main(args):
    for i in range(1, len(args)):
        if args[i] == '-n' or args[i] == '--new':
            new_note(args[i + 1])
        elif args[i] == '-s' or args[i] == '--search':
            search_note(args[i + 1])
        elif args[i] == '-d' or args[i] == '--delete':
            delete_note(args[i + 1])
        elif args[i] == '-l' or args[i] == '--list':
            list_notes()

# Create a new note in the DB using the description provided
def new_note(description):
    # call the db function to create a new row
    db.insert_new_note(description)

# search a record in the db matching the provided description
def search_note(description):
    # execute the function that searches for the record
    db.search_by_description(description)

# delete a note from the DB where the description matches
# the provided description
def delete_note(description):
    # Call the db function to delete the record
    db.delete_by_description(description)

# function to API to db function to list all records
def list_notes():
    db.list_records()

# call the driver function
main(sys.argv)
