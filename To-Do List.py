tasks = []

print("===== TO-DO LIST =====")

# Add tasks
for i in range(5):
    task = input("Enter a task: ")
    tasks.append(task)

print("\nYour To-Do List:")

# Display tasks
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

# Remove a task
task_to_remove = input("\nEnter the task you want to remove: ")

if task_to_remove in tasks:
    tasks.remove(task_to_remove)
    print("Task removed successfully!")
else:
    print("Task not found!")

# Display updated list
print("\nUpdated To-Do List:")

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

