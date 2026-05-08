# Quiz game
# Version 2

print("Welcome to the general knowledge quiz game.")

score = 0
print("Question is: What is the capital of India ?")
answer = input().lower().strip()
if answer == 'delhi':
    print("Capital of India is Delhi, that is correct!")
    score = score + 1
else:
    print("Wrong answer")
print("Question is: What is the financial capital of India ?")
answer = input().lower().strip()
if answer == 'mumbai':
    print("Financial capital of India is Mumbai, that is correct!")
    score = score + 1
else:
    print("Wrong answer")
print("Question is: Biggest city in India is ?")
answer = input().split()
if answer == 'delhi':
    print("Biggest city in India is Delhi, that is correct!")
else:
    print("Wrong answer")    
print("Your score is: ", score, "/3")