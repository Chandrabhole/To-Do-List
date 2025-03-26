tasks = []
def display_menu():
    print("\n===== To_Do List Menu =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\n No tasks available.")
    else:
        print("\n Your Tasks.")
        for i, task in enumerate(tasks, start=1):
            status = "[✔️ ]" if task["completed"] else "[]"
            print(f"{i}.{status} {task["task"]}")
        
def add_task():
                task_description = input("\n Enter the task description:").strip()
                if task_description:
                    tasks.append({"task": task_description, "completed": False})
                    print("Task added successfully.")
                else:
                    print("Task description cannot be empty!")

def mark_task_completed():
                    if not tasks:
                        print("\n No tasks available to mark as completed.")
                        return
                    task_number = int(input("\n Enter the task number to mark as completed:"))
                    if 1 <=task_number <=len(tasks):
                        tasks[task_number -1]["completed"] = True
                        print("Task marked as completed.") 
                    else:
                        print("Invalid task number.")

def delete_task():
        if not tasks:
            print("\n No tasks availabe to delete.")
            return
        task_number = int(input("\n Enter the task number to delete:"))
        if 1 <= task_number <= len(tasks):
            removed_task=tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")


while True:
    display_menu()
    choice = input("\n Enter your choice (1-5):").strip()
    if choice =="1":
        view_tasks()
    elif choice =="2":
        add_task()
    elif choice =="3":
         mark_task_completed()
    elif choice =="4":
        delete_task()
    elif choice =="5":
        print("\n Existing the To_Do List. Goodbye!")
        break
    else:
        print("\n Invalid choice. Please try again.")
                                     

                    
