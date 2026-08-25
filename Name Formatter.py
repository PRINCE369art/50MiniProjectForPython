name = input ("Ente your name: ")
name_parts = name.split()
first = name_parts[0]
last = name_parts[1]

print(f"Hello, {first.title()}, {last.title()}!")

#"prince chaudhary" to ["prince", "chaudhary"]
# .title() capitalizes the first letter of each word in a string