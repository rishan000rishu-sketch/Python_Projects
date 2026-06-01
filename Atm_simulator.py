
PIN = "1234"  # This is default PIN
balance = 5000   #balance is default

# Added pin Verification method
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == PIN:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("\nToo many incorrect attempts. Account locked.")
else:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print("Current Balance: ₹", balance)

        # Deposit Money
        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))

            if amount > 0:
                balance += amount
                print("₹", amount, "deposited successfully.")
                print("Updated Balance: ₹", balance)
            else:
                print("Invalid amount!")

        # Withdraw Money
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("Invalid amount!")

            elif amount > balance:
                print("Insufficient balance!")

            else:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance: ₹", balance)

        # Exit
        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        # Invalid Choice
        else:
            print("Invalid choice! Please try again.")