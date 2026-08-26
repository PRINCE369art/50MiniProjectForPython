# i = 1 → j = 1, 2, 3, 4, 5...
# i = 2 → j = 1, 2, 3, 4, 5...
# i = 3 → j = 1, 2, 3, 4, 5...

# testing
# for i in range(5):   #i is a variable # 5 is include .
#     print(i)

# for i in range(5, 11):  # here 5 is include and 11 is exclude.
#     print(i)

# for i in range(3):
#     print("Prince")

# for i in range(3):
#     print(i)

# for i in range(2, 11, 2):  # 2 is the start, 11 is the end (exclusive), 2 is the step
#     print(i)

# for i in range(1, 11):
#     print(5 * i)

# for i in range(1, 11):
#     print(f"5 * {i} = {5*i}")  

# for table in range(1, 6):
#     for i in range(1, 11):
#         print(table * i, end="\t")
#     print()

print("===== MULTIPLICATION TABLE =====")

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()