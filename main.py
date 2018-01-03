import platform
import os

notes_file_path = ''
if platform.system() == 'Linux':
    notes_file_path = os.path.join(
        '/home', os.getlogin(), '.terminoter', 'notes'
    )

def main(args):
    for i in range(1, len(args)):
        if args[i] == '-n' or args[i] == '--new':
            new_note(args[i + 1])

def new_note(description):
    notes_file = open(notes_file_path, 'a+')
    notes_file.write(description + '\n')
    notes_file.close()

# def delete_note():

main(platform.sys.argv)
