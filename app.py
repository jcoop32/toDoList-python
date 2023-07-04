# things we need:

# if user wants to add, edit, or delete a new task
# if add -> ask what they want to add -> add to list which has a number assigned to it 
# if edit -> ask for which number of task wanted to change -> prompt for new entry
# if delete -> ask for which number of task -> remove from list
# list tasks
# exit program
# complete a task

# display a list of menu options
# user will select an option
# add- run addTask() -> return to menu
# edit - run editTask() -> return to menu
# delete - run deleteTask() -> return to menu
# complete - run completeTask() - return to menu
# exit - break loop
# read the input and call function 
# return to menu

# completeTask() -> if isDone = false -> mark complete

listItems = []

exitProgram = False



def menu():
    userChoice = input('Command: (a)dd, (e)dit, (d)elete, (c)omplete, (l)ist, (L)ist All, e(x)it: ')
    if (userChoice == 'a'):
        addTask()
        listTasks()
    elif (userChoice == 'e'):
        editTask()
    elif (userChoice == 'd'):
        deleteTask()
    elif (userChoice == 'c'):
        completeTask()
    elif (userChoice == 'l'):
        listTasks()
    elif (userChoice == 'L'):
        listAllTasks()
    elif (userChoice == 'x'):
        print('User quit')
        global exitProgram
        exitProgram = True
    else:
        print('Command not found')
    

def addTask():
    userInput = input('Enter task: ')
    task = {
        "description": userInput,
        "isDone": False,
    }
    listItems.append(task)
    print('Task added!')

def editTask():
    if (len(listItems) > 0 ):
        editChoice = input('# of task to edit: ')
        editChoice = int(editChoice)
        # check to see if task is in index
        if (len(listItems) >= editChoice):
            newTask = input(str(editChoice) + ': ')
            listItems[editChoice - 1]['description'] = newTask
        else:
            print('task not found')
    else:
        print('No items in list')

def deleteTask():
    if (len(listItems) > 0):
        deleteChoice = input('# of item to delete: ')
        deleteChoice = int(deleteChoice)
        if (len(listItems) >= deleteChoice):
            confirm = input('Are you sure you want to delete? (y/n): ')
            if (confirm.casefold() == 'y'):
                listItems.pop(deleteChoice - 1)
        else:
            print('task not found')
    else:
        print('No items in list')

def completeTask():
    if (len(listItems) > 0):
        task = input('# of Task finished: ')
        task = int(task)
        listItems[task - 1]['isDone'] = True
        print('Task completed')
    else:
        print('No items in list')

def listTasks():
    if (len(listItems) > 0):
        for i in range(0, len(listItems)):
            if (listItems[i]['isDone'] == False):
                print('---------------')
                print(str(i + 1) + ': ' + str(listItems[i]['description']))
                print('---------------')
    else:
        print('No items in list')

def listAllTasks():
    if (len(listItems) > 0):
        for i in range(0, len(listItems)):
            print('---------------')
            print(str(i + 1) + ': ' + str(listItems[i]['description']) + ' - ' + ('Completed' if (listItems[i]['isDone'] == True) else 'Not completed'))
            print('---------------')
    else:
        print('No items in list')

while (exitProgram == False):
    menu()
