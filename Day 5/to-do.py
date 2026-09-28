def save_task(task):
    # 'a' mode appends text to the file
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            print("\n--- Your Tasks ---")
            print(file.read())
    except FileNotFoundError:
        print("No task file found. Add a task first!")

# Usage
save_task("Buy groceries")
save_task("Practice Python Day 5")
view_tasks()