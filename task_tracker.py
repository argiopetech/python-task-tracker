# Requirements:
#   Text User Interface
#   Read Evaluate Print loop
#
#   Add Tasks
#   Delete Tasks when complete
#   list current tasks in the order they were added
#
#   Persist across runs (load in multiple terminals)  (chapter 7.2p
#   every user gets their own list
#   editable storage format
#   all tasks wil be entered by the user
#   user friendly
#   report # of tasks
import os
from os import system

def elicitInt(_min, _max, msg=None):
    if msg == None:
        msg = f"Enter a valid integer between {_min} and {_max}: "

    valid = False

    while not valid:
        _in = input(msg)

        try:
            _in = int(_in)

            if _min <= _in <= _max:
                valid = True
            else:
                print("Integer out of bounds")

        except ValueError:
            print("Invalid integer provided")

    return _in


def printMenu():
    print("1) Add  2) List  3) Delete  4) Count Tasks  5) Quit")


def acceptMenuInput():
    return elicitInt(1, 5, "Select a menu item: ")


allTasks = ["Task 1", "Task 2"]

def addTask(): pass
def listTasks(): pass
def deleteTask(): pass
def countTasks(): pass


def handleMenuInput(userInput):
    _quit = False

    if userInput == 1:
        addTask()
    elif userInput == 2:
        listTasks()
    elif userInput == 3:
        deleteTask()
    elif userInput == 4:
        countTasks()
    elif userInput == 5:
        _quit = True
    else:
        raise ValueError(f"Unimplemented menu item, {userInput}")

    return _quit


def main():
    _quit = False

    if os.name == 'posix':
        clearCommand = "clear"
    elif os.name == 'nt':
        clearCommand = "cls"

    system(clearCommand)

    while not _quit:
        printMenu()

        userInput = acceptMenuInput()

        system(clearCommand)

        _quit = handleMenuInput(userInput)

    print("Bye")

if __name__ == "__main__":
    main()
