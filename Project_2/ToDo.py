# A ToDo App
# Version 1
tasks = []
print("Welcome to a ToDo App")

while True:
    choice = input("1. View Tasks  2. Add Tasks  3. Remove Tasks  4. Exit App\n")
    if choice == '1':
        print(tasks)
    elif choice == '2':
        print(tasks)
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == '3':
        print(tasks)
        remove_option = input("Enter the serial number of tasks to remove: ")
        if remove_option == '1':
            tasks.remove(tasks[0])
        elif remove_option == '2':
            tasks.remove(tasks[1])
        elif remove_option == '3':
            tasks.remove(tasks[2])
        elif remove_option == '4':
            tasks.remove(tasks[3])
        elif remove_option == '5':
            tasks.remove(tasks[4])
        else:
            print("Invalid input.")
            break
        print("Task removed successfully.")

    elif choice == '4':
        print("Thanks for using the app!")
        break