# Use SQLite3 to handle the notes database
import sqlite3
# Use datetime library to insert date and time of
# new note insertion to the database
import datetime

# create a Connect object that represents the database
conn = sqlite3.connect('terminoter.db')

# create a cursor to handle the DB connection
c = conn.cursor()

# Create the databse table
def create_table():
    c.execute('''create table notes
        (date text, description text, user text)''')

def new_note(description):
    now = datetime.datetime.now()
    # change the time in text format for example:
    # '2018-01-04 20:16'
    datetime_string = now.strftime("%Y-%m-%d %H:%M")

    c.execute("""insert into notes
        values (?)""", datetime_string, description, )