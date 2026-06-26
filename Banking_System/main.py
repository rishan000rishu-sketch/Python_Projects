from accounts import (
    initialize_file,
    create_account,
    view_accounts
)

from transaction import(
    create_file,
    deposit,
    withdraw,
    check_balance,
    transaction_history
)

def menu():

    initialize_file()
    create_file()

    while True:

        print("\n===== BANKING SYSTEM =====\n")

        print("1. Create Account")
        print("2. View Accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            view_accounts()

        elif choice == "3":
            deposit()

        elif choice == "4":
            withdraw()

        elif choice == "5":
            check_balance()

        elif choice == "6":
            transaction_history()

        elif choice == "7":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

if __name__ == '__main__':
    menu()