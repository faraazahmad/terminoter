# Use SQLite3 to handle the notes database
import sqlite3

# Use datetime library to insert date and time of
# new note insertion to the database
import datetime

class Db:
    def __init__(self):
        # create a Connect object that represents the database
        self.conn = sqlite3.connect('terminoter.db')

        # create a cursor to handle the DB connection
        self.c = conn.cursor()
    
    # Create the database table
    def create_table():
        self.c.execute('''create table notes
            (date text, description text, user text)''')

    def new_note(description):
        now = datetime.datetime.now()
        # change the time in text format for example:
        # '2018-01-04 20:16'
        datetime_string = now.strftime("%Y-%m-%d %H:%M")

        self.c.execute("""insert into notes
            values (%s, %s)""", datetime_string, description)

    def search_by_description(description):
        t = (description, )
        self.c.execute("select * from notes where description=?", t)

    def close_conn():
        self.c.close()