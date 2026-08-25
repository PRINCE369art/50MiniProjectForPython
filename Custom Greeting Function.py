def greet(name, time_of_day="morning"):
    message = f"Good {time_of_day}, {name}!"
    return message

result = greet(input("Enter your name: "))
# result = greet("prince")

print(result)