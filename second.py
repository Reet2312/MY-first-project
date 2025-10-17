

import json

tasks = []

def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

def save_tasks(filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task_name, priority):
    tasks.append({"task": task_name, "priority": priority, "done": False})
    print(f"Added task: {task_name}")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    for idx, t in enumerate(tasks):
        status = "Done" if t["done"] else "Pending"
        print(f"{idx+1}. {t['task']} [Priority: {t['priority']}] Status: {status}")

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"Marked task '{tasks[index]['task']}' as done.")

def main():
    load_tasks()
    add_task("Complete GitHub project", "High")
    add_task("Write Python scripts", "Medium")
    list_tasks()
    mark_done(0)
    print("\nAfter updating:")
    list_tasks()
    save_tasks()

if __name__ == "__main__":
    main()

