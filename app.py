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
    # create obj
    task = {
        "description": userInput,
        "isDone": False,
    }
    # add obj to dictionary/array
    listItems.append(task)
    print('Task added!')

def editTask():
    editChoice = input('# of task to edit: ')
    editChoice = int(editChoice)
    # check to see if task is in index
    if (len(listItems) >= editChoice):
        # get string of new task
        newTask = input(str(editChoice) + ': ')
        # set the choice to the newtask
        listItems[editChoice - 1]['description'] = newTask
    else:
        print('task not found')

def deleteTask():
    deleteChoice = input('# of item to delete: ')
    deleteChoice = int(deleteChoice)
    if (len(listItems) >= deleteChoice):
        confirm = input('Are you sure you want to delete? (y/n): ')
        if (confirm.casefold() == 'y'):
            # delete specified task
            listItems.pop(deleteChoice - 1)
    else:
        print('task not found')

def completeTask():
    task = input('# of Task finished: ')
    task = int(task)
    if (len(listItems) >= task):
        # set the specified task to completed/true
        listItems[task - 1]['isDone'] = True
        print('Task completed')
    else:
        print('task not found')

def listTasks():
    if (len(listItems) > 0):
        for i in range(0, len(listItems)):
            # print only unfinished tasks
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
            # print all tasks and check is completed or not
            print(str(i + 1) + ': ' + str(listItems[i]['description']) + ' - ' + ('Completed' if (listItems[i]['isDone'] == True) else 'Not completed'))
            print('---------------')
    else:
        print('No items in list')

while (exitProgram == False):
    menu()
