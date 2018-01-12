# Use SQLite3 to handle the notes database
import sqlite3

# Use datetime library to insert date and time of
# new note insertion to the database
import datetime

# use os library to get the name of current user
import os

def insert_new_note(description):
    # create a Connect object that represents the database
    conn = sqlite3.connect('terminoter.db')

    # create a cursor to handle the DB connection
    c = conn.cursor()

    # get the current date and time
    now = datetime.datetime.now()
    # change the time in text format for example:
    # '2018-01-04 20:16'
    datetime_string = now.strftime("%Y-%m-%d %H:%M")

    # insert the description along with the datetime
    c.execute("""insert into notes
        values (?, ?, ?)""", (datetime_string, description, os.getlogin()))

    conn.commit()
    # close the connection
    c.close()


# Create the database table
def create_table():
    # create a Connect object that represents the database
    conn = sqlite3.connect('terminoter.db')
    # create a cursor to handle the DB connection
    c = conn.cursor()

    # create the table
    c.execute('''create table notes
        (date text, description text, user text)''')

    # close the connection
    c.close()

# search the db based on the description
def search_by_description(description):
    # create a Connect object that represents the database
    conn = sqlite3.connect('terminoter.db')
    # create a cursor to handle the DB connection
    c = conn.cursor()

    # create a tuple of description to avoid SQL injection
    t = (description, )
    # select and return the row(s) matching the description
    rows = c.execute("select * from notes where description=?", t)
    
    # TODO: clean up the following code
    # iterate over result as rows
    for record in rows:
        print(record[1])

    # TODO: handle empty result case

    # close the connection
    c.close()

# list all the records in the table
def list_records():
    # create a Connect object that represents the database
    conn = sqlite3.connect('terminoter.db')
    # create a cursor to handle the DB connection
    c = conn.cursor()

    # select all rows from the table and store the result
    rows = c.execute("select * from notes")

    # print the description of all the rows in the table
    for record in rows:
        print(record[1])

    # close the connection
    c.close()

# delete a record from the db that matches the description
def delete_by_description(description):
    # create a Connect object that represents the database
    conn = sqlite3.connect('terminoter.db')
    # create a cursor to handle the DB connection
    c = conn.cursor()

    # create a tuple of description to avoid SQL injection
    t = (description, )
    # delete the record that matches the description
    c.execute("delete from notes where description=?", t)
    # commit the changes to the db table
    conn.commit()

    # close the connection
    c.close()