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

# global listItems
listItems = []

def menu():
    user_choice = input('Command: (a)dd, (e)dit, (d)elete, (c)omplete, (l)ist, (L)ist All, e(x)it: ')
    if (user_choice == 'a'):
        addTask()
        listTasks()
    # elif (user_choice == 'e'):
    #     editTask()
    # elif (user_choice == 'd'):
    #     deleteTask()
    # elif (user_choice == 'c'):
    #     completeTask()
    # elif (user_choice == 'l'):
    #     listTask()
    # elif (user_choice == 'L'):
    #     listAllTasks()
    elif (user_choice == 'x'):
        exit()
    else:
        print('Command not found')
    

def addTask():
    user_input = input('Enter task: ')
    task = {
        "description": user_input,
        "isDone": False,
        "isDeleted": False
    }
    listItems.append(task)
    print('Task added!')

    
def listTasks():
    for i in range(0, len(listItems)):
        print('---------------')
        print(str(i + 1) + ': ' + str(listItems[i]['description']))
        print('---------------')

menu()