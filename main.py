import platform
import os
import db

notes_file_path = ''
if platform.system() == 'Linux':
    notes_file_path = os.path.join(
        '/home', os.getlogin(), '.terminoter', 'notes'
    )

def main(args):
    for i in range(1, len(args)):
        if args[i] == '-n' or args[i] == '--new':
            new_note(args[i + 1])
        elif args[i] == '-s' or args[i] == '--search'
            search_by_description()

def new_note(description):
    db_conn = Db()
    db_conn.new_note(description)
    db_conn.close_conn()

def search_note(description):
    

# def delete_note():

main(platform.sys.argv)
