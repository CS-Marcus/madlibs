#where the items will he stored
tasks = []


#determines the number of items in the list
list_counter = 0 


#gets string values only
def get_string(prompt):
    try:
        return str(input(prompt))
    except ValueError:
        print("")


#gets int values only 
def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("")


#adds a task to the to do list at a certain position
def add_Task():
    
    global list_counter

    #make sure the user doesn't enter a space
    while True:

        pos = get_string("What position of the list would you like to add to: ")

        if pos.strip() != "":
            break
        else:
            print("Please use an int \n")

    
    print("")


    #determines if the position is already occupied or not 
    while True:

        if int(pos) > list_counter: 
            break
        else: 
            print("Space is occupied\n")

        pos = get_string("What position of the list would you like to add to: ")


    
    task = get_string("Task: ")
    
    print("")
    
    #adds the task
    tasks.insert(int(pos) - 1, task)

    list_counter += 1 

    return tasks


#removes a task to the to do list at a certain position
def remove_task():
    
    #determines if the task is empty or not 
    if len(tasks) == 0:
        print("You cannot remove anything from a empty list")
        print("")
        return tasks

    #make sure the user doesn't enter a space
    while True:
        
        pos = get_string("What position of the list would you remove: ")

        if pos.strip() != "":
            break
        else:
            print("Please use an int \n")

    print("")

    #removes the index only if it is in the list 
    try:
        tasks.pop(int(pos) - 1)
        global list_counter 
        list_counter = list_counter - 1  
    except IndexError:
        print("That position is not on the list")
        print("Here is what the list looks like")
        show_list()

    return tasks 


#edits a task in the todo list 
def edit_task():

    #make sure the list isnt empty 
    if len(tasks) == 0:
        print("You cannot edit anything from a empty list \n")
        return tasks

    #make sure the user doesn't enter a space
    while True:
        
        pos = get_string("What position of the list would you like to edit to: ")

        if pos.strip() != "":
            break
        else:
            print("Please use an int \n")

    print("")
    text = get_string("Task: ")

    #determines if this index is in the list 
    try:
        tasks[int(pos) - 1] = text
    except IndexError:
        print("That position is not on the list")
        print("Here is what the list looks like")
        show_list()
    print("")


#shows the to do list 
def show_list():
    
    #determines if the list is empty 
    if len(tasks) == 0:
            print("What is there to show in an empty to do list: \n")
            return tasks

    #itterates through the list 
    for i, task in enumerate (tasks):
        
        print(f"{i+1}. {task}")
        

    print("")

def main():

    print("Welcome to the TO-DO list program\n")

    while True:

        print("To add a task press 1")
        print("To remove a task press 2")
        print("To edit a task press 3")
        print("To view the to do list press 4")
        print("To end this program press 5\n")

        print("\n")

        input = get_int("Enter number here: ")

        print("")

        if input == 5:
            print("Shutting down")
            break
    
        if input == 1:
            add_Task()

        if input == 2:
            remove_task()
            
        if input == 3:
            edit_task()

        if input == 4:
            show_list()


main()