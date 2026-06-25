from menu import view_menu, add_item
from orders import place_order
from billing import generate_bill
from reports import sales_report

def main():

     while True:

        print("\n===== RESTAURANT MANAGEMENT SYSTEM =====")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Place Order")
        print("4. Generate Bill")
        print("5. Sales Report")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            view_menu()

        elif choice == "2":
            add_item()

        elif choice == "3":
            place_order()

        elif choice == "4":
            generate_bill()

        elif choice == "5":
            sales_report()

        elif choice == "6":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
    