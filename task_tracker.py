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


def printMenu():
    print("1) Add  2) List  3) Delete  4) Count Tasks  5) Quit")


def acceptInput(): pass


def handleInput(userInput):
    print("Quitting")
    return True


def main():
    _quit = False

    while not _quit:
        printMenu()

        userInput = acceptInput()
        _quit = handleInput(userInput)


if __name__ == "__main__":
    main()
