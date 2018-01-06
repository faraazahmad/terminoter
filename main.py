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

# Create a new note in the DB using the description provided
def new_note(description):
    # create a new db connection cursor
    db_conn = Db()
    # add the record in the DB
    db_conn.new_note(description)
    # close the connection to the DB
    db_conn.close_conn()

# search a record in the db matching the provided description
def search_note(description):
    # create a new connection to the db
    db_conn = Db
    # store the result provided by sqlite and print it
    result = db_conn.search_by_description(description)
    print(result)
    # TODO: handle no result case

    # close the connection to the db
    db_conn.close_conn()

# delete a note from the DB where the description matches
# the provided description
def delete_note(description):
    # create a new connection cursor to the db
    db_conn = Db()
    # delete the record that matches the description
    db_conn.delete_by_description()
    # close the connection to the DB
    db_conn.close_conn()

# call the driver function
main(sys.argv)
