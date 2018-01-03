import sys

def main(args):
    for i in range(1, len(args)):
        if args[i] == '-n' or args[i] == '--new':
            new_note(args[i + 1])

def new_note(description):
    # TODO: Save to file

# def delete_note():

main(sys.argv)
