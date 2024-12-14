from datetime import datetime, timedelta
import json

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_recurring_task(tasks, description, state, deadline, priority, category, recurrence):
    tasks.append({"description": description, "state": state, "deadline": deadline, "priority": priority, "category": category, "recurrence": recurrence})

filename = input("Enter your personalized filename (e.g., john_tasks.txt): ")
tasks = load_tasks(filename)

print("Welcome to your To-Do List!")
selection = 0
while selection != 8:
    print("1. Add a task:")
    print("2. Delete a task:")
    print("3. View all tasks:")
    print("4. Change task state:")
    print("5. Edit task description:")
    print("6. Search tasks:")
    print("7. Add recurring task:")
    print("8. Exit:")
    selection = int(input("Enter your selection: "))
    if selection == 1:
        task_description = input("Enter the task you want to remember: ")
        deadline = input("Enter the deadline (YYYY-MM-DD): ")
        priority = input("Enter the priority (low, medium, high): ")
        category = input("Enter the category (e.g., work, personal, shopping): ")
        tasks.append({"description": task_description, "state": "pending", "deadline": deadline, "priority": priority, "category": category, "recurrence": None})
    elif selection == 2:
        task_description = input("Enter the task you want to delete: ")
        tasks = [task for task in tasks if task["description"] != task_description]
    elif selection == 3:
        tasks.sort(key=lambda x: (datetime.strptime(x["deadline"], "%Y-%m-%d"), x["priority"]))
        for task in tasks:
            deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
            state = task["state"]
            if datetime.now() > deadline and state != "completed":
                state = "delayed"
            print(f"{task['description']} - {state} - {task['deadline']} - {task['priority']} - {task['category']}")
    elif selection == 4:
        task_description = input("Enter the task you want to change the state of: ")
        new_state = input("Enter the new state (pending, paused, completed): ")
        for task in tasks:
            if task["description"] == task_description:
                task["state"] = new_state
    elif selection == 5:
        task_description = input("Enter the task you want to edit: ")
        new_description = input("Enter the new description: ")
        for task in tasks:
            if task["description"] == task_description:
                task["description"] = new_description
    elif selection == 6:
        keyword = input("Enter the keyword to search for: ")
        for task in tasks:
            if keyword.lower() in task["description"].lower():
                print(f"{task['description']} - {task['state']} - {task['deadline']} - {task['priority']} - {task['category']}")
    elif selection == 7:
        task_description = input("Enter the task you want to remember: ")
        deadline = input("Enter the deadline (YYYY-MM-DD): ")
        priority = input("Enter the priority (low, medium, high): ")
        category = input("Enter the category (e.g., work, personal, shopping): ")
        recurrence = input("Enter the recurrence (daily, weekly, monthly): ")
        add_recurring_task(tasks, task_description, "pending", deadline, priority, category, recurrence)
    elif selection == 8:
        save_tasks(filename, tasks)
        print(f"Your tasks have been saved to {filename} successfully")
        print("Goodbye, I hope to see you soon with more tasks!!!")
        break
    else:
        print("Invalid selection. Please try again:(")