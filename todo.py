# /usr/bin/python

import sys  # To work with arguments
import time  # To get current date

pendingTodoFile = "todo.txt"  # File where pending todos are stored
deletedTodoFile = "deleted.txt"  # File where deleted todos are stored
completedTodoFile = "done.txt"  # File where completed todos are stored

# Function to get current date in yyyy-mm-dd format
def getDate():
    return time.strftime("%Y-%m-%d")


# Function that returns lists of todos from file todo.txt
def getPendingTodoList():

    temp = []
    file = open(pendingTodoFile, "r")
    lines = file.readlines()

    for line in lines:
        temp.append(line.strip("\n"))

    return temp


# Function that returns lists of todos from file done.txt
def getCompletedTodoList():

    temp = []
    file = open(completedTodoFile, "r")
    lines = file.readlines()

    for line in lines:
        temp.append(line.strip("\n"))

    return temp


# Getting the command line arguments in a variable
args = sys.argv

try:
    operation = args[1]

    # Option for printing help
    if operation == "help":
        print(
            """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
        )

    # Option to list pending todos
    elif operation == "ls":

        try:
            pendingTodoList = getPendingTodoList()
            for i in range(len(pendingTodoList) - 1, -1, -1):
                print(f"[{i+1}]", pendingTodoList[i])

        except FileNotFoundError:
            print("There are no pending todos!")

    # Option to generate statistics
    elif operation == "report":

        currentDate = getDate()
        pendingTodoList = getPendingTodoList()
        completedTodoList = getCompletedTodoList()
        print(
            f"{currentDate} Pending : {len(pendingTodoList)} Completed : {len(completedTodoList)}"
        )

    # Option to add todos
    elif operation == "add":
        try:
            todoItem = args[2]
            file = open(pendingTodoFile, "a")
            file.write(f"{todoItem}\n")
            print(f'Added todo: "{todoItem}"')
        except IndexError:
            print("Error: Missing todo string. Nothing added!")
            sys.exit()

    # Option to delete todos
    elif operation == "del":

        try:
            number = int(args[2])
            pendingTodoList = getPendingTodoList()

            if (number) not in range(1, len(pendingTodoList) + 1):
                print(f"Error: todo #{number} does not exist. Nothing deleted.")

            todoItem = pendingTodoList[number - 1]
            delFile = open(deletedTodoFile, "a")
            todoItem = todoItem + "\n"
            delFile.write(todoItem)
            del pendingTodoList[number - 1]
            todoFile = open(pendingTodoFile, "w")
            for i in pendingTodoList:
                todoFile.write(f"{i}\n")

            print(f"Deleted todo #{number}")

        except IndexError:
            print("Error: Missing NUMBER for deleting todo.")
        except ValueError:
            print("Value should be an integer")

    # Option to mark todos as completed
    elif operation == "done":

        try:

            currentDate = getDate()
            number = int(args[2])
            pendingTodoList = getPendingTodoList()

            if (number) not in range(1, len(pendingTodoList) + 1):
                print(f"Error: todo #{number} does not exist.")

            todoItem = pendingTodoList[number - 1]
            doneFile = open(completedTodoFile, "a")
            doneFile.write(f"x {currentDate} {todoItem}\n")
            del pendingTodoList[number - 1]

            todoFile = open(pendingTodoFile, "w")
            for i in pendingTodoList:
                todoFile.write(f"{i}\n")

            print(f"Marked todo #{number} as done.")

        except IndexError:
            print("Error: Missing NUMBER for marking todo as done.")
        except ValueError:
            print("Value should be an integer")

except IndexError:
    print(
        """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    )
