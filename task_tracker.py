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
import sys

import os
from os import system


allTasks = []

def getFilename(user):
    return os.path.expanduser(f"~/.task-tracker-tasks{user}")


def getTasks(user):
    filename = getFilename(user)

    if not os.path.exists(filename): return []

    toReturn = []

    with open(filename) as f:
        newLine = f.readline()

        while newLine != "":
            toReturn += [newLine.strip()]

            newLine = f.readline()

    return toReturn

def writeTasks(user, tasks):
    filename = getFilename(user)

    with open(filename, "w") as f:
        for t in tasks:
            f.write(f'{t}\n')


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
    listTasks()
    print("\n1) Add  2) Delete  3) Count Tasks  4) Quit")


def acceptMenuInput():
    return elicitInt(1, 4, "Select a menu item: ")


def addTask():
    global allTasks

    task = input("Enter a task to add: ")

    allTasks += [task]


def listTasks():
    for i in range(len(allTasks)):
        print(f"{i + 1}. {allTasks[i]}")


def deleteTask():
    toDelete = elicitInt(1, len(allTasks), "Specify a task to delete: ")

    del allTasks[toDelete - 1]


def countTasks():
    print(f"\nThere are {len(allTasks)} tasks.")
    input("Press enter to continue...")


def handleMenuInput(userInput):
    _quit = False

    if userInput == 1:
        addTask()
    elif userInput == 2:
        deleteTask()
    elif userInput == 3:
        countTasks()
    elif userInput == 4:
        _quit = True
    else:
        raise ValueError(f"Unimplemented menu item, {userInput}")

    return _quit


def clearScreen():
    if os.name == 'posix':
        clearCommand = "clear"
    elif os.name == 'nt':
        clearCommand = "cls"

    system(clearCommand)


def main():
    if len(sys.argv) == 1:
        user = ""
    elif len(sys.argv) == 2:
        user = f"_{sys.argv[1]}"
    else:
        print("Provide 0 or 1 arguments")
        quit()

    global allTasks
    allTasks = getTasks(user)

    _quit = False

    while not _quit:
        clearScreen()

        printMenu()

        userInput = acceptMenuInput()

        _quit = handleMenuInput(userInput)

    writeTasks(user, allTasks)

    print("Bye")

if __name__ == "__main__":
    main()
