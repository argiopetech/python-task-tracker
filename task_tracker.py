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
import rich

allTasks = []
page = 0

PAGE_LENGTH = 15

COMPLETED   = 0
DESCRIPTION = 1

def getFilename(user):
    return os.path.expanduser(f"~/.task-tracker-tasks{user}")


def getTasks(user):
    filename = getFilename(user)

    if not os.path.exists(filename): return []

    toReturn = []

    with open(filename) as f:
        newLine = f.readline()

        while newLine != "":
            tmp = newLine.strip().split(',', maxsplit=1)
            assert(len(tmp) == 2)
            tmp[0] = tmp[0] == "True"

            toReturn += [tmp]

            newLine = f.readline()

    return toReturn

def writeTasks(user, tasks):
    filename = getFilename(user)

    with open(filename, "w") as f:
        for t in tasks:
            f.write(f'{t[0]},{t[1]}\n')


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
    print("\n1) Add  2) Complete  3) Count Tasks  4) Next Page  5) Quit")


def acceptMenuInput():
    return elicitInt(1, 5, "Select a menu item: ")


def addTask():
    global allTasks

    task = input("Enter a task to add: ")

    allTasks += [task]

def pageIndices(page):
    _min = page * PAGE_LENGTH
    _max = min((page + 1) * PAGE_LENGTH, len(allTasks))

    return (_min, _max)


def listTasks():
    (minTask, maxTask) = pageIndices(page)

    for i in range(minTask, maxTask):
        task = allTasks[i]

        if task[COMPLETED]:
            rich.print(f"[bright_black]{i + 1}. {task[DESCRIPTION]}[/bright_black]")
        else:
            print(f"{i + 1}. {task[DESCRIPTION]}")


def completeTask():
    toComplete = elicitInt(1, len(allTasks), "Specify a task to complete: ")

    allTasks[toComplete - 1][COMPLETED] = True


def countTasks():
    print(f"\nThere are {len(allTasks)} tasks.")
    input("Press enter to continue...")


def nextPageOrReset():
    global page

    (minTask, _) = pageIndices(page + 1)

    if (minTask > len(allTasks)):
        # Reset the page
        page = 0
    else:
        page += 1

def handleMenuInput(userInput):
    _quit = False

    if userInput == 1:
        addTask()
    elif userInput == 2:
        completeTask()
    elif userInput == 3:
        countTasks()
    elif userInput == 4:
        nextPageOrReset()
    elif userInput == 5:
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


def deleteComletedTasksAtListStart():
    while allTasks[0][COMPLETED]:
        del allTasks[0]


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

        deleteComletedTasksAtListStart()

        printMenu()

        userInput = acceptMenuInput()

        _quit = handleMenuInput(userInput)

    writeTasks(user, allTasks)

    print("Bye")

if __name__ == "__main__":
    main()
