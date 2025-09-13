print("Welcome to the Quiz Game!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":   # converts input to lowercase so "Yes"/"YES" also works
    quit()

print("Okay! Let's play 😊")

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
