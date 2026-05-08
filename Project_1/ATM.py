# A basic ATM

print("Welcome to a basic ATM")
print("What would you like to do today?")
balance = 1000
choice = input("1. Check balance\n2. Deposit amount\n3. Make a withdrawal\n")

if choice == '1':
    print(balance)
elif choice == '2':
    additional_amount = int(input("Enter amount to deposit: "))
    balance = balance + additional_amount
    print("Balance updated successfully")
    print("Updated balance is ", balance)
elif choice == '3':
    withdrawal_amount = int(input("Enter the amount you would like to withdraw: "))
    if withdrawal_amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - withdrawal_amount
        print("Amount debited successfully.")
        print("New balance is ", balance)
else:
    print("Please start operations again")