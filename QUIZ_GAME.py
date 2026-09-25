print("welcome to my computer quiz game: ")
playing = input("do you want to play?").lower()

if playing != "yes":
    quit()

print("okay! let's play :) ")

score = 0

answer = input("what does cpu stand for? ").lower()
if answer == "central processing unit".lower():
    print('correct!')
    score += 1
else:
    print("incorrect")

answer = input("what does gpu stand for? ").lower()
if answer == "graphic processing unit".lower():
    print('correct!')
    score += 1
else:
    print("incorrect")

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory".lower():
    print('correct!')
    score += 1
else:
    print("incorrect")

answer = input("what does psu stand for? ").lower()
if answer == "power supply".lower():
    print('correct!')
    score += 1 
else:
    print("incorrect")


print("quiz finished")
print("you got", score , "correct and", 4 - score, "incorrect")