task_list = []
while True:
    user_choice = input("What would you like to do?\nAdd task(add), view all tasks(view), set task as complete(mark), delete a task(remove), or quit(leave): ").lower()
    if user_choice == "add":
        new_task = {"name": input("Input name of task: ").lower(), "complete": False}
        task_list.append(new_task)
    elif user_choice == "mark":
        atask = input("What task should be marked complete? ").lower()
        for new_task in task_list:
            if atask == new_task["name"]:
                new_task["complete"] = True
                print("Your task has been completed :)")
                break
        else:
            print("Task could not be found :( ")
    elif user_choice == "view":
        print("Your current tasks are:")
        for a, new_task in enumerate(task_list, 1):
            if new_task["complete"] == True:
                status = "[|/]"
            else: 
                new_task["complete"] == False
                status = "[X]"    
            print(f"{a}. {new_task['name']} {status}")
    elif user_choice == "remove":
        rtask = input("What task should be deleted?").lower()
        found = False
        for task in task_list:
            if rtask == task["name"]:
                found = True
                sure = input("Are yo sure you want to delete this task?(yes, no) ").lower()
                while sure not in ["yes", "no"]:
                    print("Invalid input>: ")
                    sure = input("Are yo sure you want to delete this task?(yes, no) ").lower()
                if sure == "yes":
                    task_list.remove(task)
                    print(f"{rtask} has been removed :|")
                else:
                    print("Task not deleted.")
                    break
            if not found:
                print("Your task does not exist.")
    elif user_choice == "leave":
        break
    else:
        print("Error: Invalid choice")
