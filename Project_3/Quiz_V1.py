# Quiz game
# Version 1
print("Welcome to the general knowledge quiz game.")
print("Question is: What is the capital of India ?")

answer = input().lower().strip()    
# We can also use .capitalize() which will make the first letter capital and make other letters in lower case
# We can also use .title() which will behave like a heading of a chapter in textbook, making the first letter of each word an uppercase and rest in lowercase

if answer == 'delhi':
    print("Capital of India is Delhi, that is correct!")
else:
    print("Wrong answer")