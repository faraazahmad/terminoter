# Terminoter
A CLI in python to create and delete notes.

## Reuirements
Make sure you have python3 installed on your system.

## Installation
After cloning the repo, `cd` into it and run `install.py` like so:
```
python install.py
```
you *may* need to type  `python3` instead of `python`. This script will create the database
on the system and the table needed to store the notes.

## Features

### 1. Make notes
To make a new note, run main.py with the flag `-n` or `--new` followed by the note 
description. The notes are saved in the `~/.terminoter/notes` file. Like so:
```
$ python3 main.py -n "Here is a new note"
```

### 2. Search note(s) by description
Use the flag `-s` or `--search` to search notes by description. The description of all
notes will be returned that exactly match the provided description. 
<!-- TODO: Implement search by matching part(s) of the description -->
<!-- TODO: Implement search by ID -->

### 3. Delete note(s) by description
Use the flag `-d` or `--delete` to delete a note that exactly matches the description that
you provide in the command. Like so:
```
$ python3 main.py -d "Here is a new note"
```
<!-- TODO: Implement delete by ID -->

### 4. List all notes
Simply execute main.py with the `-l` or `--list` flag. Like so:
```
$ python3 main.py -l
```

# Contributing
Open up an issue to add a feature, issue a bug, or even if you have a PR ready first open up an 
issue, it makes feature tracking more feasible. Issue and PR template coming soon.