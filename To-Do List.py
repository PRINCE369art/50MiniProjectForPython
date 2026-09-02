tasks = []  # this make the list empty and ready to store tasks

print("===== TO-DO LIST =====")

# Add tasks
for i in range(5):                   # here the for loop is used to add 5 tasks to the list 
    task = input("Enter a task: ")
    tasks.append(task)          # append() method is used to add the task to the list

print("\nYour To-Do List:")

# Display tasks
for i, task in enumerate(tasks, start=1):  #enumerate() function is used to get the index and value of each task in the list, starting from 1
    print(f"{i}. {task}")  # print each task with its index

# Remove a task
task_to_remove = input("\nEnter the task you want to remove: ") #making tast_to_remove variable to store the task that user wants to remove from the list

if task_to_remove in tasks:  # in operator is used to check if the task is present in the list or not
    tasks.remove(task_to_remove)
    print("Task removed successfully!")
else:
    print("Task not found!")

# Display updated list
print("\nUpdated To-Do List:")

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

